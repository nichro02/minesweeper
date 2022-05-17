from tkinter import *
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
    bg='red',
    width=settings.WIDTH,
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='blue',
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0,y=utils.height_prct(25))

#run the window
root.mainloop()