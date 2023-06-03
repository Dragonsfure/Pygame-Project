# Pygame-Project

## 


## Weiterer Code 
      
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

    # # Gleich zu dieser Variante nur mit Statischer String Liste für Sicherheit
    # # Switch Statement, but python specific 
    # match self.state:       
    #   case 'menu':
    #     self.runDifficultyMenu(key)
    #   case 'ingame':
    #     self.runGame(key)
    #   case 'gameover':
    #     self.runGameOverScreen(key)
    #   case 'win':
    #     self.runWinScreen(key)
    #   case 'paused':
    #     #Do nothing, since its paused 
    #     return
