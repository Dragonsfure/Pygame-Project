import pygame as pg
from game.config import Config

# Class for the WinScreen
class WinScreen:
  # General Field
  config: Config

  # Constructor for the WinScreen  
  def __init__(self, config: Config):
    self.config = config

  # Renders the WinScreen 
  def Render(self, screen: pg.Surface):
    backgroundImage  = pg.image.load('assets/background-assets/winscreen.png')
    backgroundImage = pg.transform.scale(backgroundImage, (screen.get_width(), screen.get_height()))
    screen.fill((0, 0, 0))  # background
    screen.blit(backgroundImage, (0, 0))
