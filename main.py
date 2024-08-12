from window import Window
from drawing import (Line, Point, Cell)
from maze import Maze

def main():
    win = Window(800, 600)
    
    maze = Maze(10,10,8,8,40,40,win)

    win.wait_for_close()

main()