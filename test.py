

import tkinter
from random import randint
#this gets called every 10 ms
def periodically_called():
    color_picker=randint(1,3)
    if color_picker==1:
        color="red"
    elif color_picker==2:
        color="blue"
    else:
        color="purple"
    root.configure(background=color)
    root.after(10, periodically_called)

root = tkinter.Tk()
root.after(10, periodically_called)
root.mainloop()