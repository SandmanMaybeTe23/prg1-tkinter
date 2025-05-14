from tkinter import *
from random import randint


x_cord=0.3

move_left=0.005
move_right=0.005

left_active=False
right_active=False

enemy1_height=0
use_enemy1=True

enemy2_height=0
use_enemy2=True

enemy3_height=0
use_enemy3=True

enemy4_height=0
use_enemy4=True

two_picks=2

already_use1=False
already_use2=False
already_use3=False
already_use4=False

root = Tk()
root.title("cube mover")
root.configure(background="purple")
root.geometry("300x300")


start_box=Label(root,text="press enter to start", width=15,height=10, background="white")
start_box.place(relx = 0.5, rely = 0.5, anchor = CENTER)

enemy_spawner1=Label(root,text="", width=45,height=5, background="red")
enemy_spawner1.place(relx = 0.3, x =-2, y = enemy1_height, anchor = NE)

enemy_spawner2=Label(root,text="", width=45,height=5, background="red")
enemy_spawner2.place(relx = 0.5, x =-2, y = enemy2_height, anchor = NE)

enemy_spawner3=Label(root,text="", width=45,height=5, background="red")
enemy_spawner3.place(relx = 0.7, x =-2, y = enemy3_height, anchor = NE)

enemy_spawner4=Label(root,text="", width=46,height=5, background="red")
enemy_spawner4.place(relx = 0.9515, x =-2, y = enemy4_height, anchor = NE)


wall_right=Label(root,text="",background="indian red", width=10,height=50)
wall_right.place(relx=0.0, rely=1.0, anchor="sw")

wall_left=Label(root,text="",background="indian red", width=10,height=50)
wall_left.place(relx=0.95, rely=1.0, anchor="sw")

player_box=Label(root,text="",background="black",width=5,height=5,)
player_box.place(relx = 0.3, x =-1, y = 575, anchor = NE)



def right_key(event):
    global x_cord
    global move_right


    if x_cord < 0.95:
        x_cord+=move_right
        slow_down_right()
        move_right+=0.003
        player_box.place_configure(relx=x_cord)

    elif x_cord>=0.95:
        x_cord=0.95
        player_box.place_configure(relx=x_cord)
        print()
    else:
        print 
        

def left_key(event):
    global x_cord
    global move_left
    global left_active
    print(move_left)
    left_active=True

    if x_cord > 0.092:
        x_cord -= move_left
        slow_down_left()
        move_left+=0.003
        player_box.place_configure(relx=x_cord)

    elif x_cord <= 0.092:
        x_cord=0.092
        player_box.place_configure(relx=x_cord)
        print("")
    else:
        print


def space_left(event):
    global left_active
    global x_cord
    x_cord-=0.010
    player_box.place_configure(relx=x_cord)
    print("nyehehhehehehhehehehehehhe")


def active_checker():
    global move_left
    global move_right
    global left_active
    global right_active

    if left_active==False:
        slow_down_left()
    else:
        print()
    
    if right_active==False:
        slow_down_right()
    else:
        print
    root.after(200,active_checker)
        




    
def slow_down_left():
    global move_left

    if move_left<0.005:
        move_left=0.005
    elif move_left>0.005 and move_left<0.020:
        move_left-=0.001
    elif move_left >0.020:
        move_left-=0.003
    else:
        print
             
def slow_down_right():
    global move_right

    if move_right<0.005:
        move_right=0.005
    elif move_right>0.005 and move_right<0.020:
        move_right-=0.001
    elif move_right>0.020:
        move_right-=0.003
    else:
        print


def start(event):
    start_box.configure(text="",background="purple",height=-1,width=-1, )
    enemy_picker()


def enemy_picker():
    global two_picks
    global use_enemy1
    global use_enemy2
    global use_enemy3
    global use_enemy4
    global already_use1
    global already_use2
    global already_use3
    global already_use4
        
    enemy_active=randint(0,4)

    print(enemy_active)

    print(two_picks)
    

    if enemy_active==1 and two_picks!=0 and use_enemy1==True :
        two_picks-=1
        if already_use1==False:
            use_enemy1=False
            enemy1()
            already_use1=True
        else:
            use_enemy1=False

    elif enemy_active==2 and two_picks!=0 and use_enemy2==True:
        two_picks-=1
        if already_use2==False:
            use_enemy2=False
            enemy2()
            already_use2=True
        else:
            use_enemy2=False

    elif enemy_active==3 and two_picks!=0 and use_enemy3==True:
        two_picks-=1
        if already_use3==False:
            use_enemy3=False
            enemy3()
            already_use3=True
        else:
            use_enemy3=False

    elif enemy_active==4 and two_picks!=0 and use_enemy4==True:
        two_picks-=1
        if already_use4==False:
            use_enemy4=False
            enemy4()
            already_use4=True
        else:
            use_enemy4=False

    else:
        print()

    root.after(500,enemy_picker)


def enemy1():
    global enemy1_height
    global use_enemy1
    global two_picks
    
    
    if enemy1_height>575:
        enemy1_height=0
        enemy_spawner1.place_configure(y=enemy1_height)
        two_picks+=1
        use_enemy1=True

    elif use_enemy1==False:
        enemy1_height+=57.5
        enemy_spawner1.place_configure(y=enemy1_height)
    
    else:
        print
    root.after(500,enemy1)


def enemy2():
    global enemy2_height
    global use_enemy2
    global two_picks

    if enemy2_height>575:
        enemy2_height=0
        enemy_spawner2.place_configure(y=enemy2_height)
        two_picks+=1
        use_enemy2=True

    elif use_enemy2==False:
        enemy2_height+=57.5
        enemy_spawner2.place_configure(y=enemy2_height)
    
    else:
        print
    root.after(500,enemy2)


def enemy3():
    global enemy3_height
    global use_enemy3
    global two_picks

    if enemy3_height>575:
        enemy3_height=0
        enemy_spawner3.place_configure(y=enemy3_height)
        two_picks+=1
        use_enemy3=True

    elif use_enemy3==False:
        enemy3_height+=57.5
        enemy_spawner3.place_configure(y=enemy3_height)
    
    else:
        print
    root.after(500,enemy3)

def enemy4():
    global enemy4_height
    global use_enemy4
    global two_picks

    if enemy4_height>575:
        enemy4_height=0
        enemy_spawner4.place_configure(y=enemy4_height)
        two_picks+=1
        use_enemy4=True

    elif use_enemy4==False:
        enemy4_height+=57.5
        enemy_spawner4.place_configure(y=enemy4_height)
    
    else:
        print
    root.after(500,enemy4)



def game_over():
    global enemy1_height
    global x_cord

    if x_cord<=0.3 and enemy1_height>=495:
        root.destroy()

    elif x_cord <0.5300000000000001 and x_cord >0.245 and enemy2_height>=495:
        root.destroy()

    elif x_cord < 0.73 and x_cord > 0.449 and enemy3_height>=495:
        root.destroy()

    elif x_cord < 0.9525 and x_cord > 0.6964999999999998 and enemy4_height>=495:
        root.destroy()

    else:
        print

    root.after(1,game_over)
  

root.bind("<Right>", right_key )
root.bind("<Left>", left_key)
root.bind("<Return>", start )
root.bind("<Shift-KeyPress>",space_left )


game_over()
active_checker()

root.mainloop()