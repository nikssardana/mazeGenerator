# Import a library of functions called 'pygame'
import pygame
from math import pi

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN =  (  0,   255, 0)

# Set the height and width of the screen
size = [500, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Maze")


done = False #Loop until the user clicks the close button.
clock = pygame.time.Clock()
cols = 10
width = int(size[0]/cols)

class Point(object):
    def __init__(self):
        self.draw  = [True,True,True,True] #TBRL
        self.visited = False

grid = [ [ Point() for x in range(cols) ] for y in range(cols) ] #A grid of points ie rectangular boxes
grid[0][0].visited = True
current = grid[0][0]

def drawGrid():
    for x in range(cols):
        for y in range(cols):
            #TBRL
            if grid[x][y].draw[0]:
                pygame.draw.line(screen, BLACK, [(x)*width,(y)*width], [(x+1)*width,(y)*width], 5)
            if grid[x][y].draw[1]:
                pygame.draw.line(screen, BLACK, [(x)*width,(y+1)*width], [(x+1)*width,(y+1)*width], 5)
            if grid[x][y].draw[2]:
                pygame.draw.line(screen, BLACK, [(x+1)*width,(y)*width], [(x+1)*width,(y+1)*width], 5)
            if grid[x][y].draw[3]:
                pygame.draw.line(screen, BLACK, [(x)*width,(y)*width], [(x)*width,(y+1)*width], 5)

            if grid[x][y].visited:
                pygame.draw.rect(screen, BLUE, [(x)*width, (y)*width, (x+1)*width, (y+1)*width])
            if current == grid[x][y]:
                pygame.draw.rect(screen, GREEN, [(x)*width, (y)*width, (x+1)*width, (y+1)*width])


while not done:
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
    #Exit when user clicks close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    # Clear the screen and set the screen background
    screen.fill(WHITE)
    drawGrid() #Draw the grid
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
