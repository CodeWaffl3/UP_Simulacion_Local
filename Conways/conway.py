"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

from datetime import date
import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from patterns import *

ON = 255
OFF = 0
vals = [ON, OFF]

def addPoint(i,j,grid):
    grid[i,j] = ON

class GameOfLife:
    def __init__(self):
        self.Blocks = 0
        self.Beehive = 0
        self.Loaf = 0
        self.Boat = 0
        self.Blinkers = 0
        self.Toads = 0
        self.Beacons = 0
        self.Tubs = 0
        self.Gliders = 0
        self.LightWeightShips = 0

    def ResetPatternCount(self):
        self.Blocks = 0
        self.Beehive = 0
        self.Loaf = 0
        self.Boat = 0
        self.Blinkers = 0
        self.Toads = 0
        self.Beacons = 0
        self.Tubs = 0
        self.Gliders = 0
        self.LightWeightShips = 0

    def CheckAllPatterns(self, N, M, grid):
        for i in range(N):
            for j in range(M):
                for pattern in ALL_PATTERNS:
                    if checkPatterns(i, j, N, M, grid, pattern.array):
                        if pattern.name == "Block": self.Blocks += 1
                        if pattern.name == "Beehive": self.Beehive += 1
                        if pattern.name == "Loaf": self.Loaf += 1
                        if pattern.name == "Boat": self.Boat += 1
                        if pattern.name == "Blinker": self.Blinkers += 1
                        if pattern.name == "Toad": self.Toads += 1
                        if pattern.name == "Beacon": self.Beacons += 1
                        if pattern.name == "Tub": self.Tubs += 1
                        if pattern.name == "Glider": self.Gliders += 1
                        if pattern.name == "LightWeightShip": self.LightWeightShips += 1
        return self.Blocks + self.Beehive + self.Loaf + self.Boat + self.Blinkers + self.Toads + self.Beacons + self.Tubs + self.Gliders + self.LightWeightShips

def checkPatterns(i, j, N, M, grid, pattern):
    check=True
    if(i+len(pattern)-1 < N and j+len(pattern[0])-1<M):
        for h in range(len(pattern)):
            for k in range(len(pattern[0])):
                    if(grid[i+h,j+k]!=pattern[h,k]):
                        check=False
    else: check = False
    return check



conways = GameOfLife()


generations=0
first = True
def update(frameNum, img, grid, N,M):
    global first
    if(first == True): 
        first = False
        return 
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line 
    newGrid = grid.copy()
    auxGrid = grid.copy()
    auxGrid = np.pad(auxGrid,1,mode="constant")
    # TODO: Implement the rules of Conway's Game of Life
    conways.ResetPatternCount()
    sumTotal = conways.CheckAllPatterns(N, M, auxGrid)

    f = open("output.txt", "a")
    f.write("---------------------------------- \n")
    f.write("Generation: "+ str(frameNum)+ "\n\n")
    f.write("Block: " + str(conways.Blocks) +" | ")
    if(sumTotal!= 0): f.write(" "+ str(conways.Blocks/sumTotal*100)+" % "+"\n")
    else:  f.write(" "+ str(0)+" % "+"\n")
    f.write("Beehive: "+ str(conways.Beehive) +" | ")
    if(sumTotal!= 0): f.write(" "+ str(conways.Beehive/sumTotal*100)+" % "+"\n")
    else:  f.write(" "+ str(0)+" % "+"\n")
    f.write("Loaf: "+ str(conways.Loaf) +" | ")
    if(sumTotal!= 0): f.write(" "+ str(conways.Loaf/sumTotal*100)+" % "+"\n")
    else:  f.write(" "+ str(0)+" % "+"\n")
    f.write("Boat: "+ str(conways.Boat) +" | ")
    if(sumTotal!= 0): f.write(" "+ str(conways.Boat/sumTotal*100)+" % "+"\n")
    else:  f.write(" "+ str(0)+" % "+"\n")
    f.write("Tub: "+ str(conways.Tubs) +" | ")
    if(sumTotal!= 0): f.write(" "+ str(conways.Tubs/sumTotal*100)+" % "+"\n")
    else:  f.write(" "+ str(0)+" % "+"\n")
    f.write("Blinker: "+ str(conways.Blinkers) +" | ")
    if(sumTotal!= 0): f.write(" "+ str(conways.Blinkers/sumTotal*100)+" % "+"\n")
    else:  f.write(" "+ str(0)+" % "+"\n")
    f.write("Toad: "+ str(conways.Toads) +" | ")
    if(sumTotal!= 0): f.write(" "+ str(conways.Toads/sumTotal*100)+" % "+"\n")
    else:  f.write(" "+ str(0)+" % "+"\n")
    f.write("Beacon: "+ str(conways.Beacons) +" | ")
    if(sumTotal!= 0): f.write(" "+ str(conways.Beacons/sumTotal*100)+" % "+"\n")
    else:  f.write(" "+ str(0)+" % "+"\n")
    f.write("Glider: "+ str(conways.Gliders) +" | ")
    if(sumTotal!= 0): f.write(" "+ str(conways.Gliders/sumTotal*100)+" % "+"\n")
    else:  f.write(" "+ str(0)+" % "+"\n")
    f.write("LWS: "+ str(conways.LightWeightShips) +" | ")
    if(sumTotal!= 0): f.write(" "+ str(conways.LightWeightShips/sumTotal*100)+" % "+"\n")
    else:  f.write(" "+ str(0)+" % "+"\n")
    f.write("Total: "+ str(sumTotal)+"\n")

    #Update the frame for the animation
    for i in range(N):
        for j in range(M):
            neighbors = 0
            for h in range(-1, 2):
                for k in range(-1, 2):
                    # check if im in bounds
                    if (i + h >= 0 and i + h < N and j + k >= 0 and j + k < M):
                        if (h != 0 or k != 0):
                            if (grid[i + h, j + k] == ON): neighbors += 1
            if (grid[i, j] == ON):
                if (neighbors < 2): newGrid[i, j] = OFF
                if (neighbors == 2 or neighbors == 3): newGrid[i, j] = ON
                if (neighbors > 3): newGrid[i, j] = OFF
            if (grid[i, j] == OFF):
                if (neighbors == 3): newGrid[i, j] = ON
    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")


    # set animation update interval
    updateInterval = 50

    with open('input.txt', 'r') as file:
        input_lines = [line.strip() for line in file]
    x, y = input_lines.pop(0).split()
    print(x, y)
    x = int(x)
    y = int(y)
    global generations
    generations = input_lines.pop(0)
    generations = int(generations)
    # declare grid
    grid = np.array([])
    grid = np.zeros(x*y).reshape(x, y)

    #Put the initial settings
    for lines in input_lines:
        i,j = lines.split()
        i = int(i)
        j = int(j)
        addPoint(i,j,grid)
    

    # Output file
    f = open("output.txt", "w")
    f.write("Simulation at "+ str(date.today())+ "\n")
    f.write("Universe size "+ str(x)+ " x "+ str(y)+"\n")
    f.close()


    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, x, y), frames = generations, interval=updateInterval, save_count=50,repeat=False)
    plt.show()


# call main
if __name__ == '__main__':
    main()