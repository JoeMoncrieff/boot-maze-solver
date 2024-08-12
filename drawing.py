from tkinter import Canvas
import functools

def calc_center(x1,y1,x2,y2):
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2

    return Point(center_x,center_y)


class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Line():
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color = "black"):
        canvas.create_line(self.p1.x,self.p1.y,self.p2.x,self.p2.y, fill = fill_color, width=2)

class Cell():
    def __init__(self, x1, y1, x2, y2, has_top = True, has_bottom = True, has_left = True, has_right = True,window = None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.has_top = has_top
        self.has_bottom = has_bottom
        self.has_left = has_left
        self.has_right = has_right
        self.window = window
    
    def __eq__(self, c):
        return functools.reduce(lambda a,b: a and b,
        [self.x1 == c.x1,
         self.y1 == c.y1,
         self.x2 == c.x2,
         self.y2 == c.y2,
         self.has_top == c.has_top,
         self.has_bottom == c.has_bottom,
         self.has_left == c.has_left,
         self.has_right == c.has_right,
         self.window == c.window])

    def __repr__(self):
        output = f"x1: {self.x1} y1: {self.y1} x2: {self.x2} y2: {self.y2} window:{self.window}"


    def draw(self):
        # Making points here
        top_left = Point(self.x1,self.y1)
        top_right = Point(self.x2,self.y1)
        bottom_left = Point(self.x1,self.y2)
        bottom_right = Point(self.x2,self.y2)
        
        if (self.has_top):
            Line(top_left,top_right).draw(self.window.canvas)
        else:
            Line(top_left,top_right).draw(self.window.canvas,"white")
        if (self.has_bottom):
            Line(bottom_left,bottom_right).draw(self.window.canvas)
        else:
            Line(bottom_left,bottom_right).draw(self.window.canvas,"white")
        if (self.has_left):
            Line(top_left,bottom_left).draw(self.window.canvas)
        else:
            Line(top_left,bottom_left).draw(self.window.canvas,"white")
        if (self.has_right):
            Line(top_right,bottom_right).draw(self.window.canvas)
        else:
            Line(top_right,bottom_right).draw(self.window.canvas, "white")

    
    def draw_move(self,to_cell, undo = False):
        from_pnt = calc_center(self.x1,self.y1,self.x2,self.y2)
        to_pnt = calc_center(to_cell.x1,to_cell.y1,to_cell.x2,to_cell.y2)
        colour = "red"
        if undo:
            colour = "gray"
        
        Line(from_pnt,to_pnt).draw(self.window.canvas,fill_color=colour)
        
            


        