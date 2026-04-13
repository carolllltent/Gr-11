


import pygame   
pygame.init() 

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
            
SIZE = (600,600)
screen = pygame.display.set_mode(SIZE) 
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
MAGENTA = (255,0,255)
WHITE = (255,255,255)

def board():
  pygame.draw.rect(screen,BLACK, (0,0, 600, 600)) 
  pygame.draw.rect(screen, WHITE, (163, 0, 50, 600))
  pygame.draw.rect(screen, WHITE, (387, 0, 50, 600))
  pygame.draw.rect(screen, WHITE, (0, 163, 600, 50))
  pygame.draw.rect(screen, WHITE, (0, 387, 600, 50))
  pygame.display.flip() #to show board - fix comment later 
  pygame.time.delay(2000)
  
def circle(x): 
  pygame.draw.circle(screen, RED, (x, 82), 70, 15) 
  #draw circle using pygame.draw.circle(screen, RED, (x,y), r, t)
  pygame.display.flip()
  pygame.time.delay(2000)

def cross(x,y): 
  pygame.draw.line(screen, BLUE, (x, y), (x + 130, y + 115), 15)
  pygame.draw.line(screen, BLUE, (x + 130 ,y), (x, y + 115), 15)
  #draw line using pygame.draw.circle(sceen, BLUE, (x,y), (w, h), t)
  pygame.display.flip()
  pygame.time.delay(2000)

#call functions for the delay to watch the game in real time 
board()
circle(82)
cross(453, 457)
circle(300)
cross(243, 246)
circle(520)

pygame.draw.line(screen, MAGENTA, (20, 83), (585, 83), 15)
pygame.display.flip()
  
#x = 453
#y = 457 
#x1 = 243
#y1 = 246 

# pygame.draw.circle(screen, RED, (82, 82), 70, 15) 
# pygame.draw.circle(screen, RED, (300, 82), 70, 15)
# pygame.draw.circle(screen, RED, (520, 82), 70, 15)
