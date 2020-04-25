import pygame
from game_state import GameState

pygame.init()  #происходит инициация 
game = GameState()



while True:
    for i in pygame.event.get():   #evens содержит список событии
        if i.type == pygame.QUIT:  #цикл обработки событии
            pygame.quit()  #завершает
            break

    keys = pygame.key.get_pressed()  #снимает маску  зажатых клавиш
    game.process()    
    game.hero.move(keys)   
    game.draw()  
    

    pygame.display.flip()  #обновление экрана

