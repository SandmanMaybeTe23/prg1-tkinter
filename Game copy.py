from tkinter import *
from random import randint

root = Tk()
root.title("light show")
color="white"
stopper=False



def On():
    global stopper
    stopper=False
    light_button.configure(text="Off",command=Off)
    color_changer()
    


def Off():
    global stopper
    stopper=True
    light_button.configure(text="On",command=On)
    color="white"
    root.configure(background=color)




def color_changer():
    global stopper
    if stopper==False:
        color_changer=randint(1,3)
        if color_changer==1:
            color="red"
        elif color_changer==2:
            color="blue"
        else:
            color="purple"
        root.configure(background=color)
        root.after(10,On)
    else:
          print("")
        











            
                
                  
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


root.after_idle(10,On)
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