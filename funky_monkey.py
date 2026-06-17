import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)
from pygame import *

init()
SIZE = 1000, 700
screen = display.set_mode(SIZE)
clock = time.Clock()

level = "loading"
currentLevel = "level1"
#where to restart after death 
fontHello = font.SysFont("Monospaced", 70)
     
mountain1Pic = image.load("mountains1.png")
mountain1Pic = transform.scale(mountain1Pic, (1000, 700))
#mountain 

monkey1Pic = image.load("monkey.png")
monkey1Pic = transform.scale(monkey1Pic, (100, 120))
#monkey 

monkey2Pic = image.load("monkey.png")
monkey2Pic = transform.scale(monkey1Pic, (300, 360))
#monkey 

buttonPic = image.load("button.png")
buttonPic = transform.scale(buttonPic, (200, 200)) 
button2Pic = image.load("button.png")
button2Pic = transform.scale(buttonPic, (200, 200)) 
#buttons 

boss1Pic = image.load("boss1.png")
boss1Pic = transform.scale(boss1Pic, (180, 200))
#boss 1 

boss2Pic = image.load("boss2.png")
boss2Pic = transform.scale(boss2Pic, (180, 200))

bulletPic = image.load("bullet.png")
bulletPic = transform.scale(bulletPic, (150, 100 ))
#bullet 

titlePic = image.load("title.png")
titlePic = transform.scale(titlePic, (650, 433))
#title 

help1Pic = image.load("help1.png")
help1Pic = transform.scale(help1Pic, (300, 300))
help2Pic = image.load("help2.png")
help2Pic = transform.scale(help2Pic, (300, 300))
help3Pic = image.load("help3.png")
help3Pic = transform.scale(help3Pic, (300, 300))
help4Pic = image.load("help4.png")
help4Pic = transform.scale(help4Pic, (300, 300))
#boards in help scene 

startPic = image.load("banana1.png")
startPic = transform.scale(startPic, (300, 300))
helpPic = image.load("banana2.png")
helpPic = transform.scale(helpPic, (300, 300))
quitPic = image.load("banana3.png")
quitPic = transform.scale(quitPic, (300, 300))
backPic = image.load("back.png")
#buttons 

deadPic = image.load("dead.png")
#death scene 

monkX = 50
monkY = 500
#monkey movement 

boss1X = 500 
boss1Y = 430
boss1speed = 1
bossHP = 4
hit_count = 0 
#boss 1 movement 

background = 0 
scrolling = 2
#scrolling background
 
velocity = 0 
gravity = 1
jump_strenght = -20
jump_counter = 0 
max_jump = 2
#jumping function 

bulletspeed = 4
bulletX = 0
bulletY = 500 
#bullet movement 

buttonX = 700
buttonY = 500
button_pressed = False
#button pressing

help1X = 500 
help2X = 1500 
help3X = 2500
help4X = 3500 
#help buttons 

spikePic = image.load("spike.png")
spikePic = transform.scale(spikePic, (150, 100))
spike_on = False 
spikeX = 0 
spikeY = boss1Y + 80 
spiketimer = 0 
#account for spike drawing and loading into game

def drawloadingScene(screen):
    screen.fill((0,0,0))
    screen.blit(mountain1Pic, (background, 0))
    screen.blit(mountain1Pic, (background + 1000, 0))
    title = (180, 50, 650, 433)
    screen.blit(titlePic, title)
    screen.blit(startPic, (200, 500))
    screen.blit(helpPic, (425, 500))
    screen.blit(quitPic, (650, 500))
    display.flip()

def drawLevel1(screen): 
    screen.fill((0,0,0))
    screen.blit(mountain1Pic, (background, 0))
    screen.blit(mountain1Pic, (background + 1000, 0))
    #draw first copy of moutain background, then draws second copy of mountain backgroudn so when first copy moves off screen, second is still visible 
    #use rect to create hitboxes for following objects so they can interact with each other 
    screen.blit(monkey1Pic, (monkX, monkY))
    screen.blit(boss1Pic, (boss1X, boss1Y))
    screen.blit(buttonPic, (buttonX, buttonY))
    #draw button 
    if button_pressed == True: 
        screen.blit(bulletPic, (bulletX, bulletY))
    #draw bullet 
    screen.blit(backPic, (20, 20))
    #shows back button for laoding screen 
    display.flip()

def drawLevel2(screen): 
    screen.fill((0,0,0))
    screen.blit(mountain1Pic, (background, 0))
    screen.blit(mountain1Pic, (background + 1000, 0))
    screen.blit(monkey1Pic, (monkX, monkY))
    screen.blit(boss2Pic, (boss1X, boss1Y))
    screen.blit(button2Pic, (buttonX, buttonY))
    #draw button 
    screen.blit(backPic, (20, 20))
    if spike_on == True: 
        screen.blit(spikePic, (spikeX, spikeY))
    #when button is pressed, spike is drawn 
    display.flip()
    
def drawHelp(screen): 
    screen.fill((0,0,0))
    screen.blit(mountain1Pic, (background, 0))
    screen.blit(mountain1Pic, (background + 1000, 0))
    screen.blit(help1Pic, (help1X, 360))
    screen.blit(help2Pic, (help2X, 360))
    screen.blit(help3Pic, (help3X, 360))
    screen.blit(help4Pic, (help4X, 360))
    screen.blit(monkey1Pic, (monkX, monkY))
    screen.blit(backPic, (20, 20))
    #shows back button for loading screen 
    display.flip()

def drawDie(screen): 
    screen.blit(deadPic, (0,0))
    text = fontHello.render("You Die!", 1, (255,0,0))
    screen.blit(text, (300, 300))
    screen.blit(startPic, (350, 400))
    #allows player to restart without exiting full game 
    display.flip()

def drawWin(screen): 
    screen.fill((0,0,0))
    screen.blit(mountain1Pic, (background, 0))
    screen.blit(mountain1Pic, (background + 1000, 0))
    text = fontHello.render("You win! You saved the monkeys from the pollutants", 1, (48,25,52))
    screen.blit(text, (100, 300))
    screen.blit(monkey2Pic, (500, 300))
    display.flip()

running = True
level = "loading"

while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False

        if evnt.type == MOUSEBUTTONDOWN:
            mx, my = mouse.get_pos()
            #if button is pressed, transfer user to different level 
            if level == "loading": 
                if 200 <= mx <= 400 and 500 <= my <= 600:
                    level = "level1"
                    #start banana
                elif 425 <= mx <= 625 and 500 <= my <= 600:
                    level = "help"
                        #help banana
                elif 650 <= mx <= 850 and 500 <= my <= 600:
                    running = False
                        #quit banana
            elif level == "level1" or level == "level2":
                if 20 <= mx <= 120 and 20 <= my <= 120:
                    level = "loading"
                    bossHP = 4
                    boss1X = 500
                    boss1speed = 1
                    hit_count = 0
                    button_pressed = False
                    bulletX = 0
                    monkX = 50
                    monkY = 500
                    spikeX = 450 
                    spikeY = 500
                    spike_on = False
                    #restart progress from level 1 when moves to loading screen 
            elif level == "help":
                if 20 <= mx <= 120 and 20 <= my <= 120:
                    level = "loading"
                    #if back button is pressed in help screen, takes user back to loading screen 
            elif level == "death": 
                 if 350 <= mx <= 650 and 400 <= my <= 700:
                    level = currentLevel
                    #saves what level user was currently at 
                    monkX = 50
                    monkY = 500
                    velocity = 0
                    jump_counter = 0
                    button_pressed = False
                    spike_on = False
                    bulletX = 0
                    bulletY = boss1Y + 80 
                    boss1X = 500 
                    boss1speed = 1 
                    bossHP = 4
                    hit_count = 0 
                    buttonX = 700 
                    button_pressed = False 
                    spikeX = 450
                    spikeY = 560
                    #restarts all progress of said level, e.g. if user had 3 hits on boss, it is now 0 hits after death 
        if evnt.type == KEYDOWN:
            if evnt.key == K_SPACE and jump_counter < max_jump:
                velocity = jump_strenght
                jump_counter += 1
        #allows for monkey to double jump through pressing space twice rather than holding otherwise, if held, it is accounted twice and double jump feature doesnt work 
    if level == "level1": 
        boss1X += boss1speed
        velocity += gravity
        monkY += velocity
        #adding monkey jupming 
        if monkY >= 500:
            monkY = 500
            velocity = 0
            jump_counter = 0 
        #landing monkey
        if monkX > 900: 
            monkX = 900
        if monkX < 0: 
            monkX = 0
        #account for monkey hitting boundaries 
        if bulletX >= 900: 
            bulletX = 50
            bulletY = 500
            button_pressed = False 
        #account for bullet hitting boundaries 
        if boss1X >= 800: 
            boss1X = 800 
            boss1speed *= -1
        if boss1X <= 0: 
            boss1X = 0 
            boss1speed *= -1
        #account for boss hitting boundaries and moving back and forth 
        monkeyHit = Rect(monkX + 25, monkY + 15, 50, 90)
        bossHit = Rect(boss1X + 30, boss1Y + 30, 140, 180)
        buttonHit = Rect(buttonX + 60, buttonY + 20, 80, 40)
        bulletHit = Rect(bulletX, bulletY, 100, 100)
        #creating hitboxes 

        if monkeyHit.colliderect(buttonHit) and button_pressed == False: 
            button_pressed = True
            if boss1X < 500:
                bulletX = 900
                bulletspeed = -4
            else:
                bulletX = 0
                bulletspeed = 4
            bulletY = boss1Y + 80
            #bullet tracks the boss's location to line up and hit the boss 
            if buttonX == 700: 
                buttonX = 100
            elif buttonX == 100: 
                buttonX = 700
            #monkey collides with button to release bullet 
        if button_pressed == True: 
            bulletX += bulletspeed 
            bulletHit = Rect(bulletX, bulletY, 150, 100)
        #creates a seperate hitbox for bullet that can be used again because once the bullet hits the boss, it is attached to boss' hitbox 

        if bossHit.colliderect(bulletHit) and button_pressed == True:
                bossHP -= 1
                hit_count += 1
                button_pressed = False
                #restarts button 
                bulletX = 0
                bulletY = boss1Y + 80
                if hit_count == 2: 
                    boss1speed *= 2
                if bossHP <= 0: 
                    level = "level2"
                    currentLevel = "level2"
                    #switches level to level 2 
                    monkX = 50 
                    monkY = 500 
                    boss1X = 500 
                    boss1speed = 1
                    bossHP = 4
                    hit_count = 0 
                    buttonX = 700 
                    button_pressed = False 
                    spike_on = False 
                    spikeX = 450
                    spikeY = 560
                    #resets spikes, boss hp, and monkey as it enters a new stage 

        if monkeyHit.colliderect(bossHit): 
            currentLevel = "level1"
            level = "death"
            #current Level is set to level to restart at level one if death happens 
    
    if level == "level2": 
        currentLevel = "level2"
        boss1X += boss1speed
        velocity += gravity
        monkY += velocity
        #adding monkey jupming 
        if monkY >= 500:
            monkY = 500
            velocity = 0
            jump_counter = 0 
        #landing monkey
        if monkX > 900: 
            monkX = 900
        if monkX < 0: 
            monkX = 0
        #account for monkey hitting boundaries 
        if bulletX >= 900: 
            bulletX = 50
            bulletY = 500
            button_pressed = False 
        #account for bullet hitting boundaries 
        if boss1X >= 800: 
            boss1X = 800 
            boss1speed *= -1
        if boss1X <= 0: 
            boss1X = 0 
            boss1speed *= -1

        monkeyHit = Rect(monkX + 25, monkY + 15, 50, 90)
        boss2Hit = Rect(boss1X + 30, boss1Y + 30, 140, 180)
        buttonHit = Rect(buttonX + 60, buttonY + 20, 80, 40)
        spikeHit = Rect(spikeX, spikeY, 150, 100)
        #creating hitboxes 
        
        if monkeyHit.colliderect(buttonHit) and spike_on == False:
            spike_on = True
            spikeX = 425
            spikeY = 560

            if buttonX == 700:
                buttonX = 100
            elif buttonX == 100:
                buttonX = 700

        if spike_on == True:
            spikeHit = Rect(spikeX, spikeY, 150, 100)
            #creates hitbox to check for different conditions 
            if boss2Hit.colliderect(spikeHit):
                bossHP -= 1
                hit_count += 1
                spike_on = False
                if hit_count == 2:
                    boss1speed *= 2
                if bossHP <= 0:
                    level = "win"
            #boss will run into spikes 
        
        if monkeyHit.colliderect(boss2Hit):
            currentLevel = "level2"
            level = "death"
            #set to level two to prepare for death instead of restarting at level 1

    if level == "help": 
        velocity += gravity
        monkY += velocity
        if monkY >= 500:
            monkY = 500
            velocity = 0
            jump_counter = 0
        if monkX < 0:
            monkX = 0
        if help4X <= 500:
            help4X = 500
        #allows monkey to move while it passes by different images and boards 

    background -= scrolling 
    #background will move to the left 
    if background <= -1000: 
        background = 0 
    #creaintg scrolling background 
    #if the first moutain background is gone, it resets to 0 
    keys = key.get_pressed()
    if keys[K_ESCAPE]:
        running = False
    if level in ["level1", "level2", "win"]:
        if keys[K_RIGHT]: 
            monkX += 5
        elif keys[K_LEFT]: 
            monkX -= 5
    elif level == "help": 
        if keys[K_RIGHT]:
            help1X -= 5
            help2X -= 5
            help3X -= 5
            help4X -= 5
        elif keys[K_LEFT]:
            help1X += 5
            help2X += 5
            help3X += 5
            help4X += 5
    #movement of monkey and boards as it leads to continous and fluid movement without pressing the keys and instead only holding 
    #monkey does not move in help like it does in level 1, 2, or win because the monkey moves too fast for the help boards 
    if level == "loading":
        drawloadingScene(screen)
    elif level == "level1":
        drawLevel1(screen)
    elif level == "level2": 
        drawLevel2(screen)
    elif level == "help":
        drawHelp(screen)
    elif level == "win": 
        drawWin(screen)
    elif level == "death": 
        drawDie(screen)
    #if level is designated level, the corresponding function is run to draw them out 
    clock.tick(60)

quit()