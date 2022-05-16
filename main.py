from tkinter import *

#instatiate window instance
root = Tk()
# window settings
#configure background color
root.configure(bg="black")
#change size of window
root.geometry('1440x720')
root.title('Minesweeper')
#prevent resizing window
root.resizable(False, False)

#create frames to structure window

#run the window
root.mainloop()