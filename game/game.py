import pygame as pg
from game.models.config import Config
from game.guiObjects.gasStation import GasStation
from game.guiObjects.enemyVehicle import EnemyVehicle
from game.guiObjects.targetBuilding import TargetBuilding
from game.guiObjects.playerVehicle import PlayerVehicle
from game.guiObjects.warehouse import Warehouse

# Game Class to handle specific Actions (like an Controller from an MVC-Pattern)
class Game:
  # General Fields
  config: Config
  gasStation: GasStation
  warehouse: Warehouse
  targetBuilding: TargetBuilding
  playerVehicle: PlayerVehicle
  enemyVehicle: EnemyVehicle
  isGameover: False
  isWin: False
  isPaused: False

  # Constructor for the Game-Class
  def __init__(self, config: Config):
    self.Restart(config)

  # Renders the Objects for the game (Fuel-Station, Warehouse, Store, Truck, Helicopter)
  def renderObjects(self, screen: pg.Surface):
    # Class Polymorphism Handling
    for x in (self.gasStation, self.warehouse, self.targetBuilding, 
              self.playerVehicle, self.enemyVehicle):
      x.Render(screen)

  # Renders the Game Statistics in the lower Corner 
  def renderStats(self, screen: pg.Surface, font: pg.font.Font):
    # Two font colors predefined 
    white = pg.Color(255, 255, 255)
    red = pg.Color(255, 0, 0)

    # Creates the Rectangle needed for the Statistics 
    stats = pg.draw.rect(screen, (0, 0, 0,0), (Config.width -150, 0, 150, 75), width=-1)

    # Shows all the Stats 
    screen.blit(font.render('Fuel: '+str(round(self.playerVehicle.fuel, 2)),
                True, (white) if self.playerVehicle.fuel > 20 else (red)), (stats.left, stats.top))
    screen.blit(font.render('FuelStation: '+str(round(self.gasStation.storage))+'/'+str(round(self.config.difficulty.fuelStationCapacity)),
                True, (white)), (stats.left, stats.top+15))
    screen.blit(font.render('Capacity: '+str(round(self.playerVehicle.load))+'/'+str(round(self.config.difficulty.truckCapacity)),
                True, (white)), (stats.left, stats.top+30))
    screen.blit(font.render('Warehouse: '+str(round(self.warehouse.storage))+'/'+str(round(self.config.difficulty.warehouseCapacity)),
                True, (white)), (stats.left, stats.top+45))
    screen.blit(font.render('Store: '+str(round(self.targetBuilding.storage))+'/'+str(round(self.config.difficulty.storeCapacity)),
                True, (white)), (stats.left, stats.top+60))

  # Renders the Background, Objects and Statistics with every Tick
  def Render(self, screen: pg.Surface, font: pg.font.Font):
    # Loads the game background and scales it 
    background = pg.image.load("assets/background-assets/game-background.png")
    background = pg.transform.scale(background, (self.config.width,self.config.height))
    # Draws the background 
    screen.fill((0, 0, 0))  # background
    screen.blit(background, (0, 0))
    #Draws the Objects and then the statistics afterwards
    self.renderObjects(screen)
    self.renderStats(screen, font)

  # reset all values to default
  def Restart(self, config: Config):
    # Resets the Values of the Objects and such with creating new Instances
    self.config = config
    self.gasStation = GasStation(config)
    self.warehouse = Warehouse(config)
    self.targetBuilding = TargetBuilding(config)
    self.playerVehicle = PlayerVehicle(config)
    self.enemyVehicle = EnemyVehicle(config)
    self.isGameover = False
    self.isWin = False
    self.isPaused = False

  # main game loop to do things with objects and check for win/loose
  def Handle(self):
    # Moves the enemy Vehicle to the last known of the Players Vehicle
    self.enemyVehicle.MoveTo(self.playerVehicle.x, self.playerVehicle.y)

    # refuel truck when entering fuel station
    if self.gasStation.rect.colliderect(self.playerVehicle.rect):
      self.playerVehicle.Refuel(self.gasStation)

    # load truck when entering warehouse
    if self.warehouse.rect.colliderect(self.playerVehicle.rect):
      self.playerVehicle.Load(self.warehouse)

    # unload truck when entering store
    if self.targetBuilding.rect.colliderect(self.playerVehicle.rect):
      self.playerVehicle.Unload(self.targetBuilding)

    # steal from truck when helicopter is over it
    if self.playerVehicle.rect.colliderect(self.enemyVehicle.rect):
      self.playerVehicle.Steal()

    # check for game over (player can not win anymore)
    if self.playerVehicle.fuel <= 0 or self.playerVehicle.load+self.warehouse.storage < self.config.difficulty.storeCapacity - self.targetBuilding.storage:
      self.isWin = False
      self.isGameover = True

    # check for win
    if self.targetBuilding.storage >= self.config.difficulty.storeCapacity:
      self.isGameover = False
      self.isWin = True

  # Toggles the Game Pause field
  def TogglePause(self):
    self.isPaused = not self.isPaused