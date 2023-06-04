from distutils.command.config import config
import pygame as pg
from game.models.config import Config
from game.models.difficulty import Difficulty
from game.guiObjects.gasStation import GasStation
from game.guiObjects.targetBuilding import TargetBuilding
from game.guiObjects.warehouse import Warehouse

# PlayerVehicle-Class 
class PlayerVehicle:

  #General Fields
  config: Config
  difficulty: Difficulty
  img = pg.image.load('assets/car-assets/cargo-truck.png')
  rect: pg.Rect
  x, y = 0, 0
  load = 0
  fuel = 0

  #Constructor for the PlayerVehicle
  def __init__(self, config: Config):
    self.config = config
    self.difficulty = config.difficulty
    self.img = pg.transform.scale(self.img, (60,60))
    self.x = 0
    self.y = 0
    self.rect = pg.Rect(0, 0, 40, 40)
    self.load = 0
    self.fuel = config.difficulty.truckFuelCapacity


  # Renders the PlayerVehicle with its current Position
  def Render(self, screen: pg.Surface):
    self.rect = pg.Rect(self.x, self.y, 40, 40)
    screen.blit(self.img, self.rect)

  # Refuel the PlayerVehicle
  def Refuel(self, fuelStation: GasStation):
    if self.fuel < self.difficulty.truckFuelCapacity and fuelStation.storage > 0:
      self.fuel += self.difficulty.fuelPerTick
      if self.fuel > self.difficulty.truckFuelCapacity:
        self.fuel = self.difficulty.truckFuelCapacity
      else:
        fuelStation.storage -= self.difficulty.fuelPerTick

  # Load the trunk of the PlayerVehicle with packets
  def Load(self, warehouse: Warehouse):
    if self.load < self.difficulty.truckCapacity and warehouse.storage > 0:
      self.load += self.difficulty.loadPerTick
      warehouse.storage -= self.difficulty.loadPerTick
      if(self.load > self.difficulty.truckCapacity):
        self.load = self.difficulty.truckCapacity

  # Unloads the content of the trucks trunk
  def Unload(self, store: TargetBuilding):
    if self.load > 0 and self.load-self.difficulty.unloadPerTick >= 0 and store.storage < self.difficulty.storeCapacity:
      self.load -= self.difficulty.unloadPerTick
      store.storage += self.difficulty.loadPerTick

  # Decreases the value of the trunk, if the helicopter is Eligible to steal the content 
  def Steal(self):
    if self.load > 0:
      self.load -= self.difficulty.helicopterStealPerTick

  # Moves the PlayerVehicle according to the pressed key/keys
  def Move(self, key):
    if (key[pg.K_UP] or key[pg.K_w]) and self.y > 0:
      self.y -= self.difficulty.truckSpeed
      self.fuel -= self.difficulty.fuelConsumptionPerMove
    if (key[pg.K_DOWN] or key[pg.K_s]) and self.y + 40 < self.config.height:
      self.y += self.difficulty.truckSpeed
      self.fuel -= self.difficulty.fuelConsumptionPerMove
      if self.y + 40 > self.config.height:
        self.y = self.config.height - 40
    if (key[pg.K_LEFT] or key[pg.K_a]) and self.x > 0:
      self.x -= self.difficulty.truckSpeed
      self.fuel -= self.difficulty.fuelConsumptionPerMove
    if (key[pg.K_RIGHT] or key[pg.K_d]) and self.x + 40 < self.config.width:
      self.x += self.difficulty.truckSpeed
      self.fuel -= self.difficulty.fuelConsumptionPerMove
      if self.x + 40 > self.config.width:
        self.x = self.config.width - 40
