import pygame as pg
from game.models.config import Config

# Class for the WinScreen
class WinScreen:
  # General Field
  config: Config

  # Constructor for the WinScreen  
  def __init__(self, config: Config):
    self.config = config

  # Renders the WinScreen 
  def Render(self, screen: pg.Surface):
    # Load background Image and Scale it to the Screen
    backgroundImage  = pg.image.load('assets/background-assets/winscreen.png')
    backgroundImage = pg.transform.scale(backgroundImage, (screen.get_width(), screen.get_height()))

    # Fills the screen first with black background then with the background 
    screen.fill((0, 0, 0))  # background
    screen.blit(backgroundImage, (0, 0))
