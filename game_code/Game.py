import pygame

from game_code.Const import WIN_WIDTH, WIN_HEIGHT
from game_code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))


    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            #for event in pygame.event.get():
                #if event.type == pygame.QUIT: #pegar o evento
                    #pygame.quit() #fechar a janela
                    #quit() #end pygame