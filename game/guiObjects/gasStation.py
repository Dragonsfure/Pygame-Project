import random
import pygame as pg
from game.models.config import Config

class GasStation:
  #General Fields
  img = pg.image.load('assets/objects-assets/gas-station.png')
  rect: pg.Rect = None
  storage = 0

  #Constructor for the Fuel-Station
  def __init__(self, config: Config):
    self.img = pg.transform.scale(self.img, (80, 80))
    x = random.randrange(10, 100)
    y = random.randrange(10, 100)
    self.rect = pg.Rect(x, y, 70, 90)
    self.storage = config.difficulty.fuelStationCapacity

  #Render Method for the Fuel-Station
  def Render(self, screen: pg.Surface):
    screen.blit(self.img, self.rect)