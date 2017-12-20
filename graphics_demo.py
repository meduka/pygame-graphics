# Imports
import pygame
import math

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
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
SKY = (170, 255, 250)
REDD = (255, 0, 1)
BROWN = (122, 44, 4)
BROWNNN = (122, 44, 0)

    

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
    pygame.draw.rect(screen, BROWN, [200, 200, 100, 200])
    pygame.draw.arc(screen, GREEN, [100, 100, 100, 100], 0, math.pi/2, 50)




    '''
    pygame.draw.ellipse(screen, WHITE, [25, 25, 450, 450])
    pygame.draw.ellipse(screen, WHITE, [100, 100, 300, 300])
    pygame.draw.ellipse(screen, WHITE, [200, 200, 100, 100])
    '''

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    pygame.draw.arc(screen, ORANGE, [700, 25, 100, 800], 0, math.pi/2, 50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
