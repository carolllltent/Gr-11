import pygame   
pygame.init() 

SIZE = (600,600)
screen = pygame.display.set_mode(SIZE) 
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
WHITE = (255,255,255)

pygame.draw.rect(screen,WHITE, (0,0, 600, 600)) 
pygame.draw.rect(screen, BLACK, (200, 0, 50, 600))
pygame.draw.rect(screen, BLACK, (350, 0, 50, 600))
pygame.draw.rect(screen, BLACK, (0, 200, 600, 50))
pygame.draw.rect(screen, BLACK, (0, 350, 600, 50))
pygame.display.flip()
pygame.time.delay(6500)

pygame.quit()

