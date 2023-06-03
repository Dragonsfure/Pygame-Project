import pygame as pg
from game.models.config import Config

# GameOverScreen Class
class GameOverScreen:
  # General Fields
  config: Config

  # Constructor for the GameOverScreen
  def __init__(self, config: Config):
    self.config = config

  # Renders the GameOverScreen
  def Render(self, screen: pg.Surface):
    # Load background Image and Scale it to the Screen
    backgroundImage  = pg.image.load('assets/background-assets/gameover.png')
    backgroundImage = pg.transform.scale(backgroundImage, (screen.get_width(), screen.get_height()))
    
    # Fills the screen first with black background then with the background 
    screen.fill((0, 0, 0))  # background
    screen.blit(backgroundImage, (0, 0))