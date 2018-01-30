# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Rain Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
STARS = (193, 238, 255)
GRAY = (116, 122, 132)


# Make clouds

daytime = True

num_clouds = 50
clouds = []
for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 200)
    loc = [x, y]
    clouds.append(loc)

def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])




    
def make_rain(r):
    pygame.draw.ellipse(screen, STARS, r)

rain = []
for i in range(800):
    x = random.randrange(-1600, 800)
    y = random.randrange(-1600, 400)
    r = random.randrange(1, 5)
    s = [x, y, r, r,]
    rain.append(s)



   
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                daytime = not daytime
    
    # Game logic
    for c in clouds:
        c[0] += 1

        if c[0] > 900:
           c[0] = random.randrange(-1600, -100)
           c[1] = random.randrange(-50, 200)
           
    ''' set sky color '''
    if daytime:
        sky = BLUE
        cloud_color = WHITE
    else:
        sky = GRAY
        cloud_color = GRAY


 
    for n in rain:
        n[1] += 10
        n[0] += 2


        if n[1] > 800:
           n[0] = random.randrange(-1600, 1600)
           n[1] = random.randrange(-500, -50)



    # Drawing code
    ''' sky '''
    screen.fill(sky)

    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])
    
    '''rain'''
    for n in rain:
        make_rain(n)



    
    ''' sun
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])
    '''
    ''' clouds''' 
    for c in clouds:
        draw_cloud(c)
    
    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
