from tkinter import *
x_cord=0.1
y_cord=1.0
anchoring="sw"
backer_x=False
root = Tk()
root.title("cube mover")
root.configure(background="purple")
root.geometry("300x300")

wall_right=Label(root,text="",background="indian red", width=10,height=50)
wall_right.place(relx=0.0, rely=1.0, anchor="sw")

wall_left=Label(root,text="",background="indian red", width=10,height=50)
wall_left.place(relx=0.95, rely=1.0, anchor="sw")

text_box=Label(root,text="",background="black",width=5,height=5)
text_box.place(relx = x_cord, 
                 rely = y_cord, 
                 anchor =anchoring)



def right_key(event):
    global x_cord

    if x_cord < 0.9  :
        x_cord+=0.01
        text_box.place_configure(relx=x_cord)
    elif x_cord>0.9:
        print()
        

def left_key(event):
    global x_cord

    if x_cord > 0.1:
        x_cord-=0.01
        text_box.place_configure(relx=x_cord)
    elif x_cord < 0.1:
        print("") 


def up_key(event):
    global y_cord
    if y_cord==1.0:
        y_cord+=2
    else:
        print


def physics():
    global y_cord
    time=0
    if y_cord>1.0:
        y_cord-=1*time
        time+=1    
    elif y_cord==1.0:
        print
    else:
        print
    root.after(10,physics)
     
        




root.bind("<Right>", right_key )
root.bind("<Left>", left_key)
root.bind("<Up>")









root.mainloop()