from tkinter import *
from random import randint


root = Tk()
root.title("light show")
color="white"
on_or_off=1
stopper=False



def change_color():
    global on_or_off
    if on_or_off==1:
        on_or_off=2
        light_button.configure(text="Off")
        color_picker=randint(1,3)
        if color_picker==1:
                color="blue"
        elif color_picker==2:
             color="red"
        else:
             color ="purple" 
        root.configure(background=color) 
        root.after(10,change_color)

    elif on_or_off == 2:
        on_or_off=1
        light_button.configure(text="On")
        
     

 




light_button=Button(root,text="On",width=50,command=change_color)
light_button.pack()


root.after_idle(10,change_color)
root.mainloop()




