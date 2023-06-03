import random
import pygame as pg
from game.models.config import Config

class TargetBuilding:
  #General Fields
  img = pg.image.load('assets/objects-assets/office-building.png')
  rect: pg.Rect = None
  storage = 0

  #Constructor for the TargetBuilding
  def __init__(self, config: Config):
    self.img = pg.transform.scale(self.img, (70, 70))
    x = random.randrange(round(config.width/2), config.width-100)
    y = random.randrange(round(config.height/2)+100, config.height-100)
    self.rect = pg.Rect(x, y, 70, 70)
    self.storage = 0

  #Renders the TargetBuilding
  # Object
  def Render(self, screen: pg.Surface):
    screen.blit(self.img, self.rect)