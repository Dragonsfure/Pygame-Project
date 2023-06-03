import pygame as pg
from game.config import Config

# GameOverScreen Class
class GameOverScreen:
  # General Fields
  config: Config

  # Constructor for the GameOverScreen
  def __init__(self, config: Config):
    self.config = config

  # Renders the GameOverScreen
  def Render(self, screen: pg.Surface):
    font = pg.font.Font(None, 60)
    screen.fill((200, 0, 0))
    text = font.render("Game Over!", True, (255, 255, 255))
    textRect = text.get_rect(
        center=(self.config.width/2, self.config.height/2))
    screen.blit(text, textRect)