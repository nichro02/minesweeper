from tkinter import *
from cell import Cell
import settings
import utils


#instatiate window instance
root = Tk()
# window settings
#configure background color
root.configure(bg="black")
#change size of window
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper')
#prevent resizing window
root.resizable(False, False)

#create frames to structure window
top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0,y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)

#instantiate game cells

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_obj(center_frame)
        c.cell_btn_object.grid(
            column = x,
            row = y
        )

#Call label to count cells from Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0,
    y=0
)

Cell.randomize_mines()
#verify cells became mines
# for c in Cell.all:
#     print(c.is_mine)

#run the window
root.mainloop()