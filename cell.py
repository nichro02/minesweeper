#This file is used to create the cells of the game
from tkinter import Button
import random

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
            height=4,
            text=f"{self.x}, {self.y}"
        )
        #assign left-click event to button
        btn.bind('<Button-1>', self.left_click_actions)
        self.cell_btn_object = btn

        #assign right-clickevent to button
        btn.bind('<Button-2>', self.right_click_actions)
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print(event)
        print('Left click!')
    
    def right_click_actions(self, event):
        print(event)
        print('Right click!')

    #static methods
    @staticmethod
    def randomize_mines():
        # my_list = ['Jim', 'Mike', 'Paul']
        # names = random.sample(my_list, 2)
        # print(names)
        picked_cells = random.sample(
            Cell.all,
            9
        )
        print(picked_cells)

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"