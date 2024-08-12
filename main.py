from window import Window
from drawing import (Line, Point, Cell)
from maze import Maze

def main():
    win = Window(800, 800)
    
    maze = Maze(10,10,16,16,40,40,win)
    maze.break_walls_i()
    maze.solve_a_star()
    
    win.wait_for_close()

main()