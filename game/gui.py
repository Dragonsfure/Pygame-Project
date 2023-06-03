import pygame as pg
from game.config import Config
from game.game import Game
from game.screens.gameover import GameOverScreen
from game.screens.menu import Menu
from game.screens.winScreen import WinScreen

# this class handles the user interface including all screens and user inputs
class Gui:
  # General Fields
  config: Config
  screen = None
  clock = None
  font = None
  state = 'menu'  # menu | ingame | paused | gameover | win
  menu = Menu()
  game: Game = None
  gameoverScreen: GameOverScreen = None
  winScreen: WinScreen = None

  #Constructor for the Gui-Class   
  def __init__(self, pg: pg):
    self.config = Config()
    self.config.difficulty.SetDifficulty(0)
    self.screen = pg.display.set_mode(self.config.clientSize)
    self.clock = pg.time.Clock()
    self.font = pg.font.Font(None, 20)
    self.state = 'menu'
    self.game = Game(self.config)
    self.gameoverScreen = GameOverScreen(self.config)
    self.winScreen = WinScreen(self.config)

  # Runs the Menu for the DifficultySelection
  def runDifficultyMenu(self, key):
    if key[pg.K_1]:
      self.config.difficulty.SetDifficulty(0)
      self.game.Restart(self.config)
      self.state = 'ingame'
    if key[pg.K_2]:
      self.config.difficulty.SetDifficulty(1)
      self.game.Restart(self.config)
      self.state = 'ingame'
    if key[pg.K_3]:
      self.config.difficulty.SetDifficulty(2)
      self.game.Restart(self.config)
      self.state = 'ingame'

    self.menu.Render(self.screen, self.font)

  # Runs the Game itself with key forwarding
  def runGame(self, key): 
    self.game.truck.Move(key)
    self.game.Loop()
    if self.game.isGameover:
      self.state = 'gameover'
    if self.game.isWin:
      self.state = 'win'

    self.game.Render(self.screen, self.font)

  # Handles the key press in the GameOverScreen
  def runGameOverScreen(self, key):
    if key[pg.K_ESCAPE]:
      self.state = 'menu'

    self.gameoverScreen.Render(self.screen)

  # Handles the key press in the Winning Screen 
  def runWinScreen(self, key):
    if key[pg.K_ESCAPE]:
      self.state = 'menu'

    self.winScreen.Render(self.screen)

  # Handles General all Actions (Main-Loop)
  def Loop(self, key):
    # Escapes back to the Menu
    if key[pg.K_ESCAPE]:
      self.state = 'menu'

    # Pauses the Game
    if key[pg.K_p]: 
      self.state = 'paused'
      self.game.TogglePause()
      if self.game.isPaused == False:
        self.state = 'ingame'

    # Switch Statement, but python specific 
    match self.state:       
      case 'menu':
        self.runDifficultyMenu(key)
      case 'ingame':
        self.runGame(key)
      case 'gameover':
        self.runGameOverScreen(key)
      case 'win':
        self.runWinScreen(key)
      case 'paused':
        #Do nothing, since its paused 
        return
