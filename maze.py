'''This program generates a square maze of specified size.
    It uses Recursive Backtracking Method.
'''
#Import a library of functions called 'pygame'
import pygame
#For selecting a random neighbour of current cell
import random

#Initialize the game engine
pygame.init()

#Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN =  (  0,   255, 0)

#Set the height and width of the screen
size = [500, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Maze")


done = False #Loop until the user clicks the close button.
clock = pygame.time.Clock()
cols = 10 #The number of columns of the maze
width = int(size[0]/cols) #The width og each box
stack = [] #The stack of cells used for backtracking

class Box(object):
    def __init__(self):
        self.draw  = [True,True,True,True] #TBRL
        self.visited = False

grid = [ [ Box() for x in range(cols) ] for y in range(cols) ] #A grid of boxes ie rectangular boxes
grid[0][0].visited = True
currentX = 0
currentY = 0

def removeEdge(currentX,currentY,nextX,nextY):
    #Remove an edge between current and next box
    xDiff = int( currentX - nextX )
    if xDiff == 1:
        #Remove current's left and next's right
        grid[currentX][currentY].draw[3] = False
        grid[nextX][nextY].draw[2] = False
    elif xDiff == -1:
        #Remove current's right and next's left
        grid[currentX][currentY].draw[2] = False
        grid[nextX][nextY].draw[3] = False

    yDiff = int( currentY - nextY )
    if yDiff == 1:
        #Remove current's bottom and next's top
        grid[currentX][currentY].draw[0] = False
        grid[nextX][nextY].draw[1] = False
    elif yDiff == -1:
        #Remove current's top and next's bottom
        grid[currentX][currentY].draw[1] = False
        grid[nextX][nextY].draw[0] = False

#Draw the grid based on which boxes are visited and which edges of each box are to be drawn
def drawGrid():
    global currentX,currentY
    for x in range(cols):
        for y in range(cols):
            if grid[x][y].visited:
                pygame.draw.rect(screen, BLUE, [(x)*width, (y)*width, width, width])
            if currentX == x and currentY == y:
                pygame.draw.rect(screen, GREEN, [(x)*width, (y)*width, width, width])
            #TBRL
            if grid[x][y].draw[0]:
                pygame.draw.line(screen, BLACK, [(x)*width,(y)*width], [(x+1)*width,(y)*width], 5)
            if grid[x][y].draw[1]:
                pygame.draw.line(screen, BLACK, [(x)*width,(y+1)*width], [(x+1)*width,(y+1)*width], 5)
            if grid[x][y].draw[2]:
                pygame.draw.line(screen, BLACK, [(x+1)*width,(y)*width], [(x+1)*width,(y+1)*width], 5)
            if grid[x][y].draw[3]:
                pygame.draw.line(screen, BLACK, [(x)*width,(y)*width], [(x)*width,(y+1)*width], 5)

    #Set current box as visited
    grid[currentX][currentY].visited = True
    #Choose a next neighbour that has not yet been visited and set it as the current box
    nextX,nextY = selectNeighbour(currentX,currentY)
    if nextX != -1 and len(stack):
        #Push current cell to stack
        stack.append([ currentX,currentY ])
        #Remove wall between current and next box and update currentX and currentY
        removeEdge(currentX,currentY,nextX,nextY)
        currentX = nextX
        currentY = nextY
    else:
        #Remove a cell from stack and make it the current cell
        currentX,currentY = stack.pop()

def selectNeighbour(x,y):
    #Select a random neighbour out of TBRL that has not been visited and return it
    neighbours = []
    #Top neighbour
    if y>0 and not grid[x][y-1].visited:
        neighbours.append( [x,y-1] )
    #Bottom neighbour
    if y<cols-1 and not grid[x][y+1].visited:
        neighbours.append( [x,y+1] )
    #Left neighbour
    if x>0 and not grid[x-1][y].visited:
        neighbours.append( [x-1,y] )
    #Right neighbour
    if x<cols-1 and not grid[x+1][y].visited:
        neighbours.append( [x+1,y] )

    if not len(neighbours):
        return( [ -1,-1 ] )
    n = neighbours[ random.randint(0,len(neighbours)-1) ]
    return n

while not done:
    #This limits the while loop to a max of n times per second.
    #Leave this out and we will use all CPU we can.
    clock.tick(5)
    #Exit when user clicks close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    #Clear the screen and set the screen background
    screen.fill(WHITE)
    drawGrid() #Draw the grid
    #Go ahead and update the screen with what we've drawn.
    #This MUST happen after all the other drawing commands.
    pygame.display.flip()
