#This file is used to create the cells of the game
from tkinter import Button, Label
import random
import settings

class Cell:
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    #create list to contain game cells
    all = []
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        #Append object to Cell.all list
        Cell.all.append(self)

    def create_btn_obj(self, location):
        btn = Button(
            location,
            width=12,
            height=4
        )
        #assign left-click event to button
        btn.bind('<Button-1>', self.left_click_actions)
        self.cell_btn_object = btn

        #assign right-clickevent to button
        btn.bind('<Button-2>', self.right_click_actions)
        self.cell_btn_object = btn

    #create label to display number of cells left in game (not instance method because it's just used to count)
    @staticmethod
    def create_cell_count_label( location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells Left: {Cell.cell_count}",
            font=("Arial", 30)
        )
        Cell.cell_count_label_object = lbl
        return lbl

    def left_click_actions(self, event):
        #print(event)
        if self.is_mine:
            self.show_mine()
        else:
            #automatically show surrounding cells if clicked cell has zero nearby mines
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

    #method to get nearby mines when a cell is clicked
    def get_cell_by_axis(self, x, y):
        #return cell object based on a and y values
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    #convert list of surrounding cells to read-only
    @property
    def surrounded_cells(self):
        #cells surrounding clicked cell
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        #filter out None cells
        cells = [cell for cell in cells if cell is not None]

        print(cells)
        return cells

    #count number of mines nearby to click cell
    @property
    def surrounded_cells_mines_length(self):
       counter = 0

       for cell in self.surrounded_cells:
           if cell.is_mine:
                counter += 1

       return counter
       
    def show_cell(self):
        Cell.cell_count -= 1
        self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)

        #Update cell count label
        if Cell.cell_count_label_object:
            Cell.cell_count_label_object.configure(text=f"Cells Left: {Cell.cell_count}")
        print('SURROUNDING CELLS',self.surrounded_cells)

        print('# NEARBY MINES',self.surrounded_cells_mines_length)   
    
    def show_mine(self):
        #write logic to end game and display message
        self.cell_btn_object.configure(bg='red', text='MINE!')
        # self.cell_btn_object.configure(text='MINE')
        print('MINE!')
    
    def right_click_actions(self, event):
        print(event)
        print('Right click!')

    #static methods
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all,
            settings.MINES_COUNT
        )
        
        #iterate over list
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"