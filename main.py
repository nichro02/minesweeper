from tkinter import *
import settings

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
    width=1440,
    height=180
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='blue',
    width=360,
    height=540
)
left_frame.place(x=0,y=180)

#run the window
root.mainloop()