from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.root_widget = Tk()
        self.canvas = Canvas(self.root_widget, width=width,height=height,background="white")
        self.is_running = False

        self.root_widget.title("Maze Solver")
        self.canvas.pack()
        

        # Sets the window to close when close method is called
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.is_running = True

        while(self.is_running):
            self.redraw()
    
    def close(self):
        self.is_running = False
        
        