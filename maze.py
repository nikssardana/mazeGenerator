# Import a library of functions called 'pygame'
import pygame
from math import pi

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)

# Set the height and width of the screen
size = [500, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Maze")

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
cols = 10
width = int(size[0]/cols)

def drawGrid():
    for x in range(cols):
        for y in range(cols):
            #TBRL
            pygame.draw.line(screen, BLACK, [(x)*width,(y)*width], [(x+1)*width,(y)*width], 5)
            pygame.draw.line(screen, BLACK, [(x)*width,(y+1)*width], [(x+1)*width,(y+1)*width], 5)
            pygame.draw.line(screen, BLACK, [(x+1)*width,(y)*width], [(x+1)*width,(y+1)*width], 5)
            pygame.draw.line(screen, BLACK, [(x)*width,(y)*width], [(x)*width,(y+1)*width], 5)

while not done:
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
    # Clear the screen and set the screen background
    screen.fill(WHITE)

    drawGrid()
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
