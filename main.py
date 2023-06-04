import sys
import pygame as pg

# Imports tge Gui class necessary for the Handling of the Interface and the Actions
# Its like the View in an MVC-Pattern (Model_View_Controller)
from game.gui import Gui

#Initialization of PyGame. 
pg.init()

#Set Pygame-Window Name.
pg.display.set_caption("Transport Spiel Efdal-Aktas")
gameGui = Gui(pg)

#Main-Loop
while True: 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    #Get Key-pressed in pygame-Window and do Task.
    key = pg.key.get_pressed()
    gameGui.Handle(key)

    #Update the Ui, with specified Ui-Elements.
    pg.display.update()
    
    #Code that prevents the framerate from exceeding 60 fps.
    gameGui.clock.tick(60)     