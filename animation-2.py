# Imports
import pygame

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Moving Block"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#image
birb1 = pygame.image.load('birb1.png')
birb2 = pygame.image.load('birb2.png')
birb3 = pygame.image.load('birb3.png')


flying_bird = [birb1, birb2, birb3]


# Block
loc = [380, 280]
vel = [0, 0]
speed = 5

def draw_block(loc, frame):
    x = loc[0]
    y = loc[1]
    screen.blit(flying_bird[frame],(x, y))

    
# Game loop
done = False

ticks = 0
frame = 0

'''
while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                vel[0] = speed
            elif event.key == pygame.K_LEFT:
                vel[0] =    -1 * speed
            elif event.key == pygame.K_UP:
                vel[1] = -1 * speed
            elif event.key == pygame.K_DOWN:
                vel[1] = speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                vel[0] = 0
            elif event.key == pygame.K_LEFT:
                vel[0] = 0
            elif event.key == pygame.K_UP:
                vel[1] = 0
            elif event.key == pygame.K_DOWN:
                vel[1] = 0'''

    # Game logic
    loc[0] += vel[0]
    loc[1] += vel[1]


    ticks += 1

    if ticks%20 == 0:
        frame += 1
        if frame > 0:
            frame = 0
            
    # Drawing code
    screen.fill(BLACK)
    draw_block(loc, frame)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
