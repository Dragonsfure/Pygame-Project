import pygame as pg
from game.models.config import Config
from game.game import Game
from game.views.gameover import GameOverScreen
from game.views.menu import Menu
from game.views.winScreen import WinScreen
from game.models.gameStates import GameStates

# this class handles the user interface including all screens and user inputs
class Gui:
  # General Fields
  config: Config
  screen = None
  clock = None
  font = None
  state = GameStates.States[0]  # menu | ingame | gameover | win | paused 
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
    self.state = GameStates.States[0] 
    self.game = Game(self.config)
    self.gameoverScreen = GameOverScreen(self.config)
    self.winScreen = WinScreen(self.config)

  # Runs the Menu for the DifficultySelection
  def runDifficultyMenu(self, key):
    if key[pg.K_1]:
      self.config.difficulty.SetDifficulty(0)
      self.game.Restart(self.config)
      self.state = GameStates.States[1] 
    if key[pg.K_2]:
      self.config.difficulty.SetDifficulty(1)
      self.game.Restart(self.config)
      self.state = GameStates.States[1] 
    if key[pg.K_3]:
      self.config.difficulty.SetDifficulty(2)
      self.game.Restart(self.config)
      self.state = GameStates.States[1] 

    # Renders the Menu of the Game
    self.menu.Render(self.screen, self.font)

  # Runs the Game itself with key forwarding
  def runGame(self, key): 
    # Moves the Truck with the Keystroke
    self.game.playerVehicle.Move(key)

    # Handles the Game Actions
    self.game.Handle()
    if self.game.isGameover:
      self.state = GameStates.States[2]
    if self.game.isWin:
      self.state = GameStates.States[3]

    # Renders the Game and its Objects
    self.game.Render(self.screen, self.font)

  # Handles the key press in the GameOverScreen
  def runGameOverScreen(self, key):
    if key[pg.K_ESCAPE]:
      self.state = GameStates.States[0]

    # Renders the GameOverScreen
    self.gameoverScreen.Render(self.screen)

  # Handles the key press in the Winning Screen 
  def runWinScreen(self, key):
    if key[pg.K_ESCAPE]:
      self.state = GameStates.States[0]
    # Renders the WinScreen
    self.winScreen.Render(self.screen)

  # Handles General all Actions (Main-Loop)
  def Loop(self, key):
    # Escapes back to the Menu
    if key[pg.K_ESCAPE]:
      self.state = GameStates.States[0]

    # Pauses the Game
    if key[pg.K_p]: 
      # Sets the game State to "paused" 
      self.state = GameStates.States[4]
      self.game.TogglePause()
      if self.game.isPaused == False:
        # Unset's the game state if its not paused anymore  
        self.state = GameStates.States[1] 

    # If Statement to decide the Action to handle the Current State of the Game    
    if  self.state == GameStates.States[0] :
        # state = Menu
        self.runDifficultyMenu(key)
    elif self.state == GameStates.States[1] :
        # state = ingame       
       self.runGame(key)
    elif self.state == GameStates.States[2] :
        # state = gameover        
        self.runGameOverScreen(key)
    elif self.state == GameStates.States[3] :
        # state = win        
        self.runWinScreen(key)
    elif self.state == GameStates.States[4] :
        # state = paused        
        return