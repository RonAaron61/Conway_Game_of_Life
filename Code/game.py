"""
Conway game of life

Rule:
1. Any live cell with fewer than two live neighbours dies (referred to as underpopulation or exposure).
2. Any live cell with more than three live neighbours dies (referred to as overpopulation or overcrowding).
3. Any live cell with two or three live neighbours lives, unchanged, to the next generation.
4. Any dead cell with exactly three live neighbours will come to life.

More Info: https://conwaylife.com/wiki/Conway%27s_Game_of_Life

How to use:
-First you can input your the size and sum of the X and Y axis of the block, and input the fps
-If the size of the calculated window of the game is bigger then your screen size (resolution) then it will pop a warning message
-You can stick with your window size or change it
-After that you can click on the grid available to input your first lives block (you can put as many lives as you want)
-To start the game play the start button, and pause button to pause the game
-For now if you want to restart the game you have to quit the game first and reopen it

https://github.com/RonAaron61/Conway_Game_of_Life
"""
import sys
import pygame
import numpy as np

BGcolor = (200, 200, 200)   #Color for background
BTcolor = (0, 0, 0)         #Button color
Maincolor = (0, 0, 0)       #Color for the main life

_event_ = 1
top_size = 40   #Create some space for the top to place button
#fps = 8

def main():
    opening() #=> input your starter life here

    pygame.display.set_caption("Game of Life")
    #pygame.init()
    clock = pygame.time.Clock()

    play = pygame.image.load('play.png').convert_alpha()
    pause = pygame.image.load('pause.png').convert_alpha()

    screen.fill(BGcolor)

    start_button = Button(15, 2, play).draw()   #Draw button
    pause_button = Button(75, 2, pause).draw()   #Draw button
    Game_pause = 1

    #Create your first life
    while _event_ == True:
        starter()
        
    #Game start
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if (((pos[1]-top_size)//blockSize < 0) and (75 < pos[0] <= 121)):
                    Game_pause = Game_pause * (-1)
                    print("Pause ", Game_pause)

            if event.type == pygame.QUIT:
                print("Game Quit")
                pygame.quit()
                sys.exit()

        if Game_pause > 0:
            rules() #Check the rules of the block available

        check() #Draw the block
        pygame.display.update()
        clock.tick(fps)
    

def opening():
    global screen, blockSize, X, Y, block, block2, fps

    #Get input about the size of the grid and screen size
    #Twisted ==> X => Y
    blockSize = int(input("block size: "))
    X = int(input("Number of X boxes: "))
    Y = int(input("Number of Y boxes: "))
    fps = int(input("FPS: "))

    #Screen size is the total of grid
    WINDOW_HEIGHT = Y*blockSize
    WINDOW_WIDTH = X*blockSize

    pygame.init()
    width = pygame.display.Info().current_w
    height = pygame.display.Info().current_h

    while ((width < WINDOW_WIDTH) or ((height - 100) < WINDOW_HEIGHT)):
        i = input("\nWarning window size is bigger then your monitor size, continue? (y/n) ")
        if i == 'n':
            blockSize = int(input("block size: "))
            X = int(input("Number of X boxes: "))
            Y = int(input("Number of Y boxes: "))

            #Screen size is the total of grid
            WINDOW_HEIGHT = Y*blockSize
            WINDOW_WIDTH = X*blockSize

        elif i == 'y':
            break

        else:
            print("Please input 'y' or 'n' only")

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT + top_size))
    
    #Create array 
    #I assuiming the np array is like Y,X matrix
    block = np.zeros(shape = (Y, X))
    block2 = np.zeros(shape = (Y, X))
    print(len(block[0]), len(block))


def starter():
    global _event_
    #Get the coordinates of input
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            y = ((pos[1] - top_size) // blockSize)
            x = (pos[0] // blockSize)
            #print(x, y)
            if (y >= 0) and (x >= 0):
                #print(x, y)
                block2[y][x] = 1

            #If mouse pressed play button the game start
            elif (y < 0 and (15 < pos[0] <= 61)):
                _event_ = 0
                print("Game Start")
        
        if event.type == pygame.QUIT:
            print("Game Quit")
            pygame.quit()
            sys.exit()

    check()
    pygame.display.update()

#To Draw
def check():    
    for i in range(Y):
        for j in range(X):
            rect = pygame.Rect(j*blockSize, i*blockSize + top_size, blockSize, blockSize)

            #If life exist draw white boxes
            if block2[i][j] == True:  
                pygame.draw.rect(screen, Maincolor, rect)

            #If there's no life draw black boxes (white grid only)
            else:
                pygame.draw.rect(screen, BGcolor, rect)
                
            pygame.draw.rect(screen, Maincolor, rect, 1)

    #Restore the value from block2 to block
    for i in range(Y):
        for j in range (X):
            block[i][j] = block2[i][j]      

#To check the block and rules
def rules():
    t = 0
    for i in range(Y):
        for j in range(X):
            #Check if there is life around
            num = 0

            #Check for the 3 row above
            for k in range (j-1, j+2):
                #If the row above is outside of the boundry then skip
                if ((k < 0) or (k >= X) or ((i-1) < 0)):
                    continue

                elif block[i-1][k] == True:
                    num += 1      

            #Check for the 3 row below
            for k in range (j-1, j+2):
                #If the row below is outside of the boundry then skip
                if ((k < 0) or (k >= X) or ((i+1) >= Y)):
                    continue

                elif block[i+1][k] == True:
                    num += 1 

            #Check for the left and right side
            for k in range (j-1, j+2, 2):
                if ((k < 0) or (k >= X)):
                    continue

                elif block[i][k] == True:
                    num += 1  

            #Check the condition if num == 3 then life born
            if num == 3:    #If there's 3 neighbor live cell will continue to live or dead cell will live
                block2[i][j] = 1

            elif (num == 2 and block[i][j] == True):    #If there is two neighbor live cell will continue to live
                block[i][j] = 1

            else:
                block2[i][j] = 0    #False

    #print(block)

class Button():
    def __init__(self, x, y, image):
        self.image = pygame.transform.scale(image, (top_size - 4, top_size - 4))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


if __name__ == "__main__":
    main()
