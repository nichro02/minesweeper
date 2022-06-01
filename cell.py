#This file is used to create the cells of the game
from tkinter import Button
import random
import settings

class Cell:
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

    def left_click_actions(self, event):
        #print(event)
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

    def show_cell(self):
        self.cell_btn_object.configure(text=f"{self.x}, {self.y}")
    
    def show_mine(self):
        #write logic to end game and display message
        self.cell_btn_object.configure(bg='red')
        self.cell_btn_object.text='MINE'
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