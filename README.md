# Maze-Generator
Generates mazes using Prim's Algorithm

## Program
This program generates `n x m` mazes using a randomized Prim's Algorithm, which is based on <a href="https://en.wikipedia.org/wiki/Maze_generation_algorithm#Randomized_Prim's_algorithm">this description</a>.

## Input
Run
```sh
python3 MazeGenerator.py <height> <width> <seed>
```
to generate a `10 x 10` maze. 

Optionally, input integer parameters
```sh
python3 MazeGenerator.py <height> <width>
```
for a `<height> x <width>` maze. 

Additionally, the program supports seeding for reproducable mazes:
```sh
python3 MazeGenerator.py <height> <width> <seed>
```

To export maze into file, use the terminal piping command:
```sh
python3 MazeGenerator.py > cool_maze.txt
```

## Reading the Output
Empty (round-edged) squares are denoted as paths. Walls are filled in rectangles. The borders are double lines. Starting point denoted `S` and end point denoted `E`. 

Here is a `4 x 4` sample:

```sh
=========
‖S▢▢▢▢▢▢‖
‖▢▬▢▬▢▬▬‖
‖▢▮▢▮▢▢▢‖
‖▢▬▢▬▬▬▢‖
‖▢▮▢▮▢▢▢‖
‖▬▬▬▬▬▬▢‖
‖E▢▢▢▢▢▢‖
=========
```
Another `100 x 100` maze is stored in `sample_maze.txt`
## Requirements
Python3 is recommended. To use a lower version, uncomment the first line to import the print function from the `__future__`.
