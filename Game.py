from tkinter import *
from random import randint


root = Tk()
root.title("light show")
color="white"
stopper=False

def stop():
    global stopper
    stopper=True

def change_color(): 
    global stopper
    if stopper== True:
        color="white"
        root.configure(background=color) 
        stopper=False

    else:
        color_picker=randint(1,3)
        if color_picker==1:
            color="red"
        elif color_picker==2:
            color="blue"
        else:
            color="purple"
        root.configure(background=color) 
        root.after(10,change_color)




light_button=Button(root,text="light button",width=50,command=change_color)
light_button.pack()
stop_button=Button(root,text="STOP",width=50,command=stop )
stop_button.pack()

root.after_idle(10,change_color)
root.mainloop()




