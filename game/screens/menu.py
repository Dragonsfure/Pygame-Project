import pygame as pg

# Menu-Class
class Menu:
  def Render(self, screen: pg.Surface, font: pg.font.Font):

    #Do Menu Background
    background = pg.image.load("assets/background-assets/menu-background.png")
    background = pg.transform.scale(background, (screen.get_width(), screen.get_height()))
    screen.fill((0, 0, 0))  # background
    screen.blit(background, (0, 0))

    # Gets the Middle Positions of the pygame-Screen/Window
    middleScreenHeight = screen.get_height()/2
    middleScreenWidth = screen.get_width()/2

    #Bigger Font :D
    newFont  = pg.font.Font(None, 30)

    # Shows the Menu in the middle of the Screen 
    screen.blit(newFont.render(
        'Transport Game by Efdal', True, (pg.Color(255, 255, 255))), (middleScreenWidth -150, middleScreenHeight -75))
    screen.blit(newFont.render(
        'Menu', True, (pg.Color(255, 255, 255))), (middleScreenWidth - 100, middleScreenHeight -25))
    screen.blit(newFont.render(
        'Press [1] to play [Easy]', True, (pg.Color(255, 255, 255))), (middleScreenWidth -100, middleScreenHeight ))
    screen.blit(newFont.render(
        'Press [2] to play [Medium]', True, (pg.Color(255, 255, 255))), (middleScreenWidth -100, middleScreenHeight + 25))
    screen.blit(newFont.render(
        'Press [3] to play [Hard]', True, (pg.Color(255, 255, 255))), (middleScreenWidth -100, middleScreenHeight +50))
