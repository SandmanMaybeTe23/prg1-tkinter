from tkinter import *
from random import randint

root = Tk()
root.title("Yea Sim")
text_box = Label(root,text="Yea")
text_box.pack()


def show():
    roll=randint(1,6)
    text_box.config(text=roll)

button= Button(root,text="Yea Destroy", width=50, command=root.destroy)
button.pack()
show_button= Button(root, text="yea",width=50, command=show)
show_button.pack()






root.mainloop()

