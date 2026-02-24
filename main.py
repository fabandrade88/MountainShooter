import pygame
print ('Setup starts')

pygame.init() #inicializar o projeto
print ('Setup Ends')

print ('Loop Starts')
window = pygame.display.set_mode(size=(600, 480))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #pegar o evento
            pygame.quit() #fechar a janela
            quit() #end pygame