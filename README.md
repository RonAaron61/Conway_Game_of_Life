# Conway Game of Life on Python

Creating the [game of life by Conway](https://conwaylife.com/wiki/Conway%27s_Game_of_Life) using python with pygame library

Conway's Game of Life, also known as the Game of Life or simply Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is the best-known example of a cellular automaton.

The "game" is actually a zero-player game, meaning that its evolution is determined by its initial state, needing no input from human players. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.

The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which (at any given time) is in one of two possible states, "live" (alternatively "on") or "dead" (alternatively "off").[1] Every cell interacts with its eight neighbours, which are the cells that are directly horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

1. Any live cell with fewer than two live neighbours dies (referred to as underpopulation or exposure[2]).
2. Any live cell with more than three live neighbours dies (referred to as overpopulation or overcrowding).
3. Any live cell with two or three live neighbours lives, unchanged, to the next generation.
4. Any dead cell with exactly three live neighbours will come to life.

The initial pattern constitutes the 'seed' of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed — births and deaths happen simultaneously, and the discrete moment at which this happens is sometimes called a tick. (In other words, each generation is a pure function of the one before.) The rules continue to be applied repeatedly to create further generations.

Preview:

<video src="https://github.com/RonAaron61/Conway_Game_of_Life/blob/main/assets/preview.mov" controls="controls" style="max-width: 730px;">
</video>

![preview](https://github.com/RonAaron61/Conway_Game_of_Life/blob/main/assets/thumb.png)

How to use the program:
- First you can input your the size and sum of the X and Y axis of the block, and input the fps
- If the size of the calculated window of the game is bigger then your screen size (resolution) then it will pop a warning message
- You can stick with your window size or change it
- After that you can click on the grid available to input your first lives block (you can put as many lives as you want)
- To start the game play the start button, and pause button to pause the game
- For now if you want to restart the game you have to quit the game first and reopen it


# Program Code

## Library

- [pygame](https://www.pygame.org/docs/)
- [numpy](https://numpy.org/)


## Code

### The Matrix

In the code I try using numpy to create the n x n array, and the order of the X and Y axis is like:

(image)

### implementing the rules

(image)
