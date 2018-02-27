# Maze-Generator
Generates mazes using Prim's Algorithm

## Program
This program generates `n x m` mazes using a randomized Prim's Algorithm, which is based on <a href="https://en.wikipedia.org/wiki/Maze_generation_algorithm#Randomized_Prim's_algorithm">this description</a>.

## Input
Run
```sh
python3 MazeGenerator.py <height> <width> <seed>
```
to generate a `10 x 10` maze. Optionally, input integer parameters
```sh
python3 MazeGenerator.py <height> <width>
```
for a `<height> x <width>` maze. Additionally, the program supports seeding for reproducable mazes:
```sh
python3 MazeGenerator.py <height> <width> <seed>
```
