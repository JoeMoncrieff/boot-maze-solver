from window import Window
from drawing import Line, Point

def main():
    win = Window(800, 600)
    
    p1,p2 = Point(300,300), Point(500,500)
    l = Line(p1,p2)
    l.draw(win.canvas)
    
    
    win.wait_for_close()

main()