from tkinter import *
from random import randint
root = Tk()
root.title("light show")
color="white"
stopper=False
click_counter=0


def On():
    
    global stopper
    global click_counter
    stopper=False
    light_button.configure(text="Off",command=Off)
    color_changer()



def Off():
    global click_counter
    global stopper    
    stopper=True 
    root.configure(background="white")
    light_button.configure(text="On",command=On)
   




    


    



def color_changer():
    global stopper
    color_change=randint(1,3)
    if color_change==1:
        color="red"
    elif color_change==2:
        color="blue"
    else:
        color="purple"
    root.configure(background=color)
    root.after(stopper==False,color_changer)


        


                              
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


light_button=Button(root,text="On",width=50,command=On)
light_button.pack()


root.after_idle(10,color_changer)
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