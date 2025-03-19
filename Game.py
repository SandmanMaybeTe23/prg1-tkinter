from tkinter import *
from random import randint
import time 


root = Tk()
root.title("light show")
text_box = Label(root,text="")
text_box.pack()

def light():



    while True:
        
        light_changer=randint(1,5)
        time.sleep(2)
        if light_changer==1:
            color="blue"
        elif light_changer ==2:
            color="red"
        elif light_changer ==3:
            color="purple"
        elif light_changer ==4:
            color="green"
        else:
            break
        root.configure(background=color) 


 



       




light_button=Button(root,text="light button",width=50, command=light  )
light_button.pack()

























root.mainloop()




