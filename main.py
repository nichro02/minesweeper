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
# c1 = Cell()
# c1.create_btn_obj(center_frame)
# c1.cell_btn_object.grid(
#     column=0,
#     row=0
# )

# c2 = Cell()
# c2.create_btn_obj(center_frame)
# c2.cell_btn_object.grid(
#     column=0,
#     row=1
# )

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell()
        c.create_btn_obj(center_frame)
        c.cell_btn_object.grid(
            column = x,
            row = y
        )

#run the window
root.mainloop()