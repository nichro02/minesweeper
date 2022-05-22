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
        self.cell_btn_object = btn