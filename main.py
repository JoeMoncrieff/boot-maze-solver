from window import Window
from drawing import (Line, Point, Cell)
from maze import Maze

def main():
    win = Window(800, 600)
    
    maze = Maze(10,10,12,12,40,40,win)
    maze.break_walls_i()
    maze.solve_dfs_i()
    

    win.wait_for_close()

main()