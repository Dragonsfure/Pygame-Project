import random
import pygame as pg
from game.config import Config

# Class for the Warehouse 
class Warehouse:
  # General Fields
  img = pg.image.load('assets/objects-assets/warehouse.png')
  rect: pg.Rect = None
  storage = 0

  # Constructor for the Warehouse
  def __init__(self, config: Config):
    self.img = pg.transform.scale(self.img, (70, 70))
    x = random.randrange(round(config.width/2), config.width-100)
    y = random.randrange(10, round(config.height/2))
    self.rect = pg.Rect(x, y, 70, 70)
    self.storage = config.difficulty.warehouseCapacity

  # Renders the Warehouse 
  def Render(self, screen: pg.Surface):
    screen.blit(self.img, self.rect)
