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
    font = pg.font.Font(None, 60)
    screen.fill((0, 200, 0))
    text = font.render("You won!", True, (255, 255, 255))
    textRect = text.get_rect(
        center=(self.config.width/2, self.config.height/2))
    screen.blit(text, textRect)
