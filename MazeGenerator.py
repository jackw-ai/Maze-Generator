# (c) 2018 Tingda Wang
# maze generator using Prim's algoirthm

''' for running on python v2 '''
# uncomment the following line to import python3 print function to python            
# from __future__ import print_function     

import random, sys

CELL = chr(0x25A2) # empty tile, represented by empty square
V_BORDER = '‖'
H_BORDER = '='
LR_WALL = chr(0x25AE) # wall separating left right cells
UD_WALL = chr(0x25AC) # wall separating front back cells
START = 'S'
END = 'E'

class MazeGenerator:

    def __init__(self, height, width, seed = 0):
        ''' initializes maze to fill it with walls'''
        self.height = height
        self.width = width
        self.maze = {}
     
        # allows seeding to regenerate maze
        if (seed is not 0):
            random.seed(seed)
    
        # multiply accounts for walls inbetween + 1 accounts for the borders
        self.row = 2 * height + 1
        self.column = 2 * width + 1
        
        # Step 1: initialize every cell to be surrounded by walls
        for i in range(self.column):
            for j in range(self.row):
                if (i % 2 == 1) and (j % 2 == 1):
                    self.maze[(i, j)] = CELL
                elif (j % 2 == 1):
                    self.maze[(i, j)] = LR_WALL
                else:
                    self.maze[(i, j)] = UD_WALL
        
        # label the borders for pretty printing
        for i in range(self.row):
            self.maze[(0, i)] = self.maze[(self.column - 1, i)] = V_BORDER
        
        for j in range(self.column):
            self.maze[(j, 0)] = self.maze[(j, self.row - 1)] = H_BORDER
         
    def add_walls(self, x, y):
        ''' get the adjacent walls of the cell at coord (x, y)'''
        for (i, j) in ((0, 1), (1, 0), (-1, 0), (0, -1)):

            # must be valid coordinates within borders
            if (i + x > 0) and (i + x < self.column - 1) and (j + y > 0) and (j + y < self.row - 1):
                if self.maze[(i + x, j + y)] == LR_WALL or self.maze[(i + x, j + y)] == UD_WALL:
                    self.wall_list.add((i + x, j + y))
        
    def generate(self):
        ''' Prim's Algorithm for maze generation as seen in Wikipedia'''
        maze_part = []
        cells = []

        # 1. fill list of cells and walls
        for i in range(self.column):
            for j in range(self.row):
                if self.maze[(i, j)] == CELL:
                    cells.append((i, j))
         
        # 2. Pick a cell, mark it as part of the maze
        start = random.choice(cells)
        maze_part.append(start)
        self.maze[start] = START

        # Add the walls of the cell to the wall list
        self.wall_list = set() # Note: we use a set to prevent duplicates
        x, y = maze_part[0]
        self.add_walls(x, y)

        # 3. While there are walls in the list:
        while(len(self.wall_list) > 0):

            # Pick a random wall from the list
            wall_i, wall_j = random.sample(self.wall_list, 1)[0]

            # wall dividing horizontally
            if self.maze[(wall_i, wall_j)] == LR_WALL:

                left_cell = (wall_i - 1, wall_j)
                right_cell = (wall_i + 1,  wall_j)

                # if only one of the two cells that the wall divides is visited
                if ((left_cell in maze_part) and (right_cell not in maze_part)) or ((left_cell not in maze_part) and (right_cell in maze_part)):

                    # Make the wall a passage
                    self.maze[(wall_i, wall_j)] = CELL

                    # mark the unvisited cell as part of the maze
                    if left_cell not in maze_part:
                        maze_part.append(left_cell)

                        # add walls of new cell to list (which is the last in list)
                        x, y = left_cell
                        self.add_walls(x, y)

                    elif right_cell not in maze_part:
                        maze_part.append(right_cell)

                        # add walls of new cell to list (which is the last in list)
                        x, y = right_cell
                        self.add_walls(x, y)

            # wall dividing vertically
            elif self.maze[(wall_i, wall_j)] == UD_WALL:

                top_cell = (wall_i, wall_j - 1)
                lower_cell = (wall_i, wall_j + 1)

                # if only one of the two cells that the wall divides is visited
                if ((top_cell in maze_part) and (lower_cell not in maze_part)) or ((top_cell not in maze_part) and (lower_cell in maze_part)):

                    # Make the wall a passage
                    self.maze[(wall_i, wall_j)] = CELL

                    # mark the unvisited cell as part of the maze
                    if top_cell not in maze_part:
                        maze_part.append(top_cell)

                        # add walls of new cell to list (which is the last in list)
                        x, y = top_cell
                        self.add_walls(x, y)

                    elif lower_cell not in maze_part:
                        maze_part.append(lower_cell)

                        # add walls of new cell to list (which is the last in list)
                        x, y = lower_cell
                        self.add_walls(x, y)
            
            # Remove the wall from the list.
            self.wall_list.remove((wall_i, wall_j))

        # set last visited cell as endpoint
        self.maze[maze_part[-1]] = END

    def __str__(self):
        ''' creates str of the maze '''
        str = ''
        str += '\n'.join(''.join(self.maze[(i, j)] for i in range(self.column)) for j in range(self.row)) 
        return str

if __name__ == '__main__':

    seed = 0
    height = width = 10
    print("This program uses Prim's Algorithm for maze generation", file = sys.stderr)
    if (len(sys.argv) > 2):
        height = int(sys.argv[1])
        width = int(sys.argv[2])
        if(len(sys.argv) > 3):
            seed = int(sys.argv[3])
    else:
        print("To specify dimensions, use command line (i.e. python3 MazeGenerator.py <height> <width>)", file = sys.stderr)
        print("The default maze dimensions are 10x10.", file = sys.stderr)
        print("Provide an optional third argument as seed for reproducable maze (i.e. python3 MazeGenerator.py <height> <width> <seed number>)\n", file = sys.stderr)

    print("Generating maze of dimensions %sx%s\n" %(height, width), file = sys.stderr)
    
    maze = MazeGenerator(height, width)
    maze.generate()
    
    print(maze)
    print("Maze successfully generated. To save the maze, pipe the program to text file (only the maze is printed to stdout)", file = sys.stderr)
    
