#This file is used to create the cells of the game
from tkinter import Button
class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None

    def create_btn_obj(self, location):
        btn = Button(
            location,
            text='Text'
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