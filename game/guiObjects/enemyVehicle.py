import pygame as pg
from game.config import Config

class EnemyVehicle:
  #General Fields
  speed = 0
  img = pg.image.load('assets/heli-assets/helicopter.png')
  rect: pg.Rect
  x, y = 0, 0

  #Constructor for the EnemyVehicle

  def __init__(self, config: Config):
    self.speed = config.difficulty.helicopterSpeed
    self.img = pg.transform.scale(self.img, (60, 60))
    self.x = config.width-40
    self.y = config.height-40
    self.rect = pg.Rect(self.x, self.y, 40, 40)

  #Moves the EnemyVehicle
  # to the Position of the Truck
  def MoveTo(self, truckX, truckY):
    if self.x > truckX:
      self.x -= self.speed
    if self.x < truckX:
      self.x += self.speed
    if self.y > truckY:
      self.y -= self.speed
    if self.y < truckY:
      self.y += self.speed

  #Renders the EnemyVehicle
  # on to the Surface
  def Render(self, screen: pg.Surface):
    self.rect = pg.Rect(self.x, self.y, 40, 40)
    screen.blit(self.img, self.rect)