# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "My Awesome Picture"
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


def draw_cloud(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])

def make_stars():
    for s in stars:
        pygame.draw.ellipse(screen, STARS, s)

stars = []
for i in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(0, 400)
    r = random.randrange(1, 5)
    stars.append([x, y, r, r,])

def draw_bird(x, y):
    for b in bird:

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

    '''
    pygame.draw.rect(screen, BROWN, [200, 200, 100, 200])
    
    
    pygame.draw.arc(screen, GREEN, [100, 100, 100, 100], 0, math.pi/2, 50)

    '''

    ''' moon '''
    pygame.draw.ellipse(screen, MOON, [575, 75, 100, 100])

  


    make_stars()
     
    '''clouds'''
    draw_cloud(50, 150)
    draw_cloud(250, 75)
    draw_cloud(150, 200)
    draw_cloud(400, 100)
    draw_cloud(540, 200)
    draw_cloud(100, 20)
    draw_cloud(640, 90)
    draw_cloud(400, 200)

    '''train'''
    y = 360
    for x in range(5, 600, 90):
        post = [[x+20, y+20], [x+40, y+20], [x+40, y+160], [x, y+160], [x, y+20]]
        pygame.draw.polygon(screen, WHITE, post)
    '''
    pygame.draw.rect(screen, WHITE, [0, y+10, 800, 5])
    pygame.draw.rect(screen, WHITE, [0, y+30, 800, 5])
    '''

    

    '''
    pygame.draw.ellipse(screen, WHITE, [25, 25, 450, 450])
    pygame.draw.ellipse(screen, WHITE, [100, 100, 300, 300])
    pygame.draw.ellipse(screen, WHITE, [200, 200, 100, 100])
    '''

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    pygame.draw.arc(screen, BROWN, [700, 25, 100, 800], 0, math.pi/2, 50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
