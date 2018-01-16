# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "Night Birds"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
GREEN = (19, 119, 32)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
SKY = (4, 18, 40)
REDD = (255, 0, 1)
BROWN = (122, 44, 4)
BROWNNN = (122, 44, 0)
STARS = (255, 255, 175)
MOON = (255, 250, 107)
YELLOW = (255, 255, 0)
BCLOUD = (153, 163, 255)
ATREETOP = (33, 99, 30)
BTREETOP = (125, 183, 123)


def draw_cloud(x, y, color):
    pygame.draw.ellipse(screen, color, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, color, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, color, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, color, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, color, [x + 20, y + 20, 60, 40])

def make_stars():
    for s in stars:
        pygame.draw.ellipse(screen, STARS, s)

stars = []
for i in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(0, 400)
    r = random.randrange(1, 5)
    stars.append([x, y, r, r,])



def draw_bird(x, y, color):
    pygame.draw.line(screen, YELLOW, [x-7, y+20],[x, y + 20], 3)
    pygame.draw.ellipse(screen, color, [x, y + 15, 15 , 15])
    pygame.draw.polygon(screen, color, [[x+10,y + 20], [x+5,y+40], [x+50, y+20]])
    pygame.draw.ellipse(screen, BLACK, [x, y + 17, 7, 7])
    
stars = []
for i in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(0, 400)
    r = random.randrange(1, 5)
    stars.append([x, y, r, r,])

def draw_treetop(x, y, color):
    pygame.draw.ellipse(screen, color, [x,y, 200, 200])


# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 

    # Drawing code (Describe the picture. It isn't actually drawn yet.)

    
    screen.fill(SKY)
    pygame.draw.rect(screen, GREEN, [0, 400, 1000, 300])

   

    ''' moon '''
    pygame.draw.ellipse(screen, MOON, [575, 75, 100, 100])

  


    make_stars()
     
    '''clouds'''
    draw_cloud(500, 150, BCLOUD)
    draw_cloud(450, 60, BCLOUD)
    draw_cloud(700, 270, BCLOUD)
    draw_cloud(400, 100, WHITE)
    draw_cloud(540, 200, WHITE)
    draw_cloud(650, 20, BCLOUD)
    draw_cloud(640, 90, WHITE)
    draw_cloud(400, 200, WHITE)



    '''fence'''

    y = 360
    
    for x in range(5, 800, 90):
        post = [[x+5, y], [x+10, y+5], [x+10, y+40], [x, y+40], [x, y+5]]
        pygame.draw.polygon(screen, WHITE, post)

    pygame.draw.rect(screen, WHITE, [0, y+10, 800, 5])
    pygame.draw.rect(screen, WHITE, [0, y+30, 800, 5])

    '''trees'''

    for x in range(20, 400, 150):
        trunk = [[x+45, y-225], [x+90, y-225], [x+90, y+60], [x, y+60], [x, y-225]]
        pygame.draw.polygon(screen, BROWN, trunk)

    draw_treetop(125,0, BTREETOP)
    draw_treetop(-30,0, ATREETOP)
    draw_treetop(270,0, ATREETOP)
    


    '''birds'''

    
    draw_bird(50, 200, RED)
    draw_bird(250, 200, YELLOW)
    draw_bird(500, 200, BLUE)


    ''' angles for arcs are measured in radians (a pre-cal topic) '''


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
