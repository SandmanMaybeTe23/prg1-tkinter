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

    if x_cord !=




root.bind("<Right>", right_key )








root.mainloop()