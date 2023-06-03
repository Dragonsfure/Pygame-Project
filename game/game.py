import pygame as pg
from game.config import Config
from game.guiObjects.gasStation import GasStation
from game.guiObjects.enemyVehicle import EnemyVehicle
from game.guiObjects.targetBuilding import TargetBuilding
from game.guiObjects.playerVehicle import PlayerVehicle
from game.guiObjects.warehouse import Warehouse

# Game Class to handle specific Actions (like an Controller from an MVC-Pattern )
class Game:
  # General Fields
  config: Config
  fuelStation: GasStation
  warehouse: Warehouse
  store: TargetBuilding
  truck: PlayerVehicle
  heli: EnemyVehicle
  isGameover: False
  isWin: False
  isPaused: False

  # Constructor for the Game-Class
  def __init__(self, config: Config):
    self.Restart(config)

  # Renders the Objects for the game (Fuel-Station, Warehouse, Store, Truck, Helicopter)
  def renderObjects(self, screen: pg.Surface):
    # Class Polymorphism Handling
    for x in (self.fuelStation, self.warehouse, self.store, 
              self.truck, self.heli):
      x.Render(screen)

  # Renders the Game Statistics in the lower Corner 
  def renderStats(self, screen: pg.Surface, font: pg.font.Font):
    white = pg.Color(255, 255, 255)
    red = pg.Color(255, 0, 0)

    stats = pg.draw.rect(screen, (0, 0, 0,255), (0, 645, 150, 75), width=1)
    screen.blit(font.render('Fuel: '+str(round(self.truck.fuel, 2)),
                True, (white) if self.truck.fuel > 20 else (red)), (stats.left, stats.top))
    screen.blit(font.render('FuelStation: '+str(round(self.fuelStation.storage))+'/'+str(round(self.config.difficulty.fuelStationCapacity)),
                True, (white)), (stats.left, stats.top+15))
    screen.blit(font.render('Capacity: '+str(round(self.truck.load))+'/'+str(round(self.config.difficulty.truckCapacity)),
                True, (white)), (stats.left, stats.top+30))
    screen.blit(font.render('Warehouse: '+str(round(self.warehouse.storage))+'/'+str(round(self.config.difficulty.warehouseCapacity)),
                True, (white)), (stats.left, stats.top+45))
    screen.blit(font.render('Store: '+str(round(self.store.storage))+'/'+str(round(self.config.difficulty.storeCapacity)),
                True, (white)), (stats.left, stats.top+60))

  # Renders the Background, Objects and Statistics with every Tick
  def Render(self, screen: pg.Surface, font: pg.font.Font):
    background = pg.image.load("assets/background-assets/game-background.png")
    background = pg.transform.scale(background, (self.config.width,self.config.height))
    screen.fill((0, 0, 0))  # background
    screen.blit(background, (0, 0))
    self.renderObjects(screen)
    self.renderStats(screen, font)

  # reset all values to default
  def Restart(self, config: Config):
    self.config = config
    self.fuelStation = GasStation(config)
    self.warehouse = Warehouse(config)
    self.store = TargetBuilding(config)
    self.truck = PlayerVehicle(config)
    self.heli = EnemyVehicle(config)
    self.isGameover = False
    self.isWin = False
    self.isPaused = False

  # main game loop to do things with objects and check for win/loose
  def Handle(self):
    
    self.heli.Move(self.truck.x, self.truck.y)

    # refuel truck when entering fuel station
    if self.fuelStation.rect.colliderect(self.truck.rect):
      self.truck.Refuel(self.fuelStation)

    # load truck when entering warehouse
    if self.warehouse.rect.colliderect(self.truck.rect):
      self.truck.Load(self.warehouse)

    # unload truck when entering store
    if self.store.rect.colliderect(self.truck.rect):
      self.truck.Unload(self.store)

    # steal from truck when helicopter is over it
    if self.truck.rect.colliderect(self.heli.rect):
      self.truck.Steal()

    # check for game over (player can not win anymore)
    if self.truck.fuel <= 0 or self.truck.load+self.warehouse.storage < self.config.difficulty.storeCapacity - self.store.storage:
      self.isWin = False
      self.isGameover = True

    # check for win
    if self.store.storage >= self.config.difficulty.storeCapacity:
      self.isGameover = False
      self.isWin = True

  # Toggles the Game Pause field
  def TogglePause(self):
    self.isPaused = not self.isPaused