from tkinter import *
from random import randint
root = Tk()
root.title("light show")
color="white"
stopper=False
root.resizable(True,True)

def click(event):
    On()
    


def On():
    global stopper
    stopper=False
    light_button.configure(text="",command=Off)
    color_changer()



def color_change_to_default():
    light_button.configure(background="white")    
    light_button.configure(text="",command=On)


def Off():
    global stopper
    stopper=True


def color_changer():
    global stopper
    color_change=randint(1,3)
    if color_change==1:
        color="red"
    elif color_change==2:
        color="blue"
    else:
        color="purple"
    light_button.configure(background=color)
    if stopper== False:
        root.after(stopper==False,color_changer)
    else:
        color_change_to_default()
    







 


                              
#def change_color():
 #   global color
  #  global stopper
   # light_button.configure(command=off)
    #if stopper !=False:
     #   color_picker=randint(1,3)
      #  if color_picker==1:
       #     color="blue"
        #elif color_picker==2:
         #   color="red"
       # else:
        #    color ="purple" 
    #root.configure(background=color)
    #root.after(10,change_color)


light_button=Button(root,text="",width=5000, height=5000,command=On)
light_button.pack()





root.mainloop()







   ##color_picker=randint(1,3)
        #if color_picker==1:
                #color="blue"
       # elif color_picker==2:
            # color="red"
       # else:
          #   color ="purple" 
       # root.configure(background=color) 
        #root.after(10,change_color)