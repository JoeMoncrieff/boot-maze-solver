from drawing import Line, Point, Cell
import time
import random

class Maze():
    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win = None, seed =None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x =cell_size_x
        self.cell_size_y = cell_size_y
        self.window = win
        if seed:
            self.seed = random.seed(seed)

        self.cells = []

        self.create_cells()
        self.break_entrance_and_exit()
        self.break_walls_i()
    
    def create_cells(self):
        self.cells = [[None] * self.num_cols for x in range(0,self.num_rows)]

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                top_x, top_y = self.x1 + (i * self.cell_size_x),self.y1 + (j * self.cell_size_y) 
                bot_x, bot_y = self.x1 + ((i+1) * self.cell_size_x), self.y1 + ((j+1) * self.cell_size_y) 
                self.cells[i][j] = Cell(top_x,top_y,bot_x,bot_y,window=self.window)
        
        if self.window:
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    self.draw_cell(i,j)


    def draw_cell(self, i, j):
        self.cells[i][j].draw()
        self.animate()

    def animate(self):
        self.window.redraw()
        time.sleep(0.05)

    def break_entrance_and_exit(self):
        #The entrance to the maze will always be at the top of the top-left cell, the exit always at the bottom of the bottom-right cell.
        self.cells[0][0].has_left = False
        self.draw_cell(0,0)
        self.cells[self.num_rows-1][self.num_cols-1].has_right  = False
        self.draw_cell(self.num_rows-1,self.num_cols-1)

    def break_walls_i(self):
        visited = []
        to_visit = [((0,0),None)]
       
        while to_visit != []:

            curr = to_visit.pop()
            current = curr[0]
            history = curr[1]
            
            adjacents = list(filter(lambda x: x not in visited, self.check_adjacent(current[0],current[1])))
            print(adjacents)
            
            if len(adjacents) != 0:
                random.shuffle(adjacents)
                for a in adjacents:
                    to_visit.append((a,current))

            #figure out which adjacent a is
            #remove the walls from both
            if history and (current not in visited) :
                a = history
                current_cell = self.cells[current[0]][current[1]]
                adjacent_cell = self.cells[a[0]][a[1]]

                if a[0] > current[0]:
                    current_cell.has_right = False
                    adjacent_cell.has_left = False
                elif a[1] > current[1]:
                    current_cell.has_bottom = False
                    adjacent_cell.has_top = False
                elif a[0] < current[0]:
                    current_cell.has_left = False
                    adjacent_cell.has_right = False
                elif a[1] < current[1]:
                    current_cell.has_top = False
                    adjacent_cell.has_bottom = False
                
                self.draw_cell(current[0],current[1])
                self.draw_cell(a[0],a[1])

                visited.append(current)            
        
    def check_adjacent(self,i,j):
        output = []
        if i - 1 >= 0:
            output.append((i-1,j))
        if i + 1 < len(self.cells):
            output.append((i+1,j))
        
        if j - 1 >= 0:
            output.append((i,j-1))
        if j + 1 < len(self.cells[0]):
            output.append((i,j+1))

        return output
    
    """
    def solve_i(self, reverse = False):
        visited = []
        to_visit = [(0,0)]
        red_line = []

        while to_visit != []:

            curr = to_visit.pop()
            current = curr[0]
            history = curr[1]
            
            adjacents = list(filter(lambda x: x not in visited, self.check_adjacent(current[0],current[1])))
            print(adjacents)
            
            if len(adjacents) != 0:
                random.shuffle(adjacents)
                for a in adjacents:
                    to_visit.append((a,current))

            #figure out which adjacent a is
            #remove the walls from both
            if history and (current not in visited) :
                a = history
                current_cell = self.cells[current[0]][current[1]]
                adjacent_cell = self.cells[a[0]][a[1]]

                if a[0] > current[0]:
                    current_cell.has_right = False
                    adjacent_cell.has_left = False
                elif a[1] > current[1]:
                    current_cell.has_bottom = False
                    adjacent_cell.has_top = False
                elif a[0] < current[0]:
                    current_cell.has_left = False
                    adjacent_cell.has_right = False
                elif a[1] < current[1]:
                    current_cell.has_top = False
                    adjacent_cell.has_bottom = False
                
                self.draw_cell(current[0],current[1])
                self.draw_cell(a[0],a[1])

                visited.append(current)
        """
