from tkinter import *

root = Tk()
root.title("clicker")
root.configure(background="brown")
money=0

cps_amount=0
cps_done=False
adding=0
cost=0
cost1=10
cost2=40
cost3=100
cost4=200
cost5=500
root.geometry("300x250")

     


def cps():
    global money
    global cps_amount

    money+=cps_amount
    show_money.configure(text=money)
    root.after(1000,cps)


def cps_add_1():
    global money
    global cps_amount
    global cost1
    global adding
    if cost1<=money:
        money-=cost1
        cost1*=2
        cps_amount+=1
        buy_upgrade.configure(text=f"{cost1}$+1 Per second")
    else:
        print



def cps_add_2():
    global money
    global cps_amount
    global cost2
    global adding
    if cost2 <= money:
        money-=cost2
        cost2*=2
        cps_amount+=2
        buy_upgrade2.configure(text=f"{cost2}$+2 Per second")
    else:
        print

def cps_add_3():
    global money
    global cps_amount
    global cost3
    global adding
    if cost3 <= money:
        money-=cost3
        cost3*=2
        cps_amount+=5
        buy_upgrade3.configure(text=f"{cost3}$+5 Per second")
    else:
        print

def cps_add_4():
    global money
    global cps_amount
    global cost4
    global adding
    if cost4<= money:
        money-=cost4
        cost4*=2
        cps_amount+=10
        buy_upgrade4.configure(text=f"{cost4}$+10 Per second")
    else:
        print

def cps_add_5():
    global money
    global cps_amount
    global cost5
    global adding
    if cost5<= money:
        money-=cost5
        cost5*=2
        cps_amount+=20
        buy_upgrade5.configure(text=f"{cost5}$+20 Per second")
    else:
        print
    
    


    
    


def clicks():
    global money
    money+=1
    show_money.configure(text=money)







show_money = Label(root,text=money,width=100,height=5, anchor="center",background="white",)
show_money.pack(padx=15,pady=150)


clicker_button=Button(root,text="+1 Per click",width=20, height=20,command=clicks)
clicker_button.pack(side=LEFT,padx=15,pady=20)

buy_upgrade=Button(root,text=f"{cost1}$+1 Per second", width=20,height=20,command= cps_add_1)
buy_upgrade.pack(side=LEFT,padx=20,pady=20)

buy_upgrade2=Button(root,text=f"{cost2}$+2 Per second", width=20,height=20,command= cps_add_2 )
buy_upgrade2.pack(side=LEFT,padx=25,pady=20)

buy_upgrade3=Button(root,text=f"{cost3}$+5 Per second", width=20,height=20,command= cps_add_3)
buy_upgrade3.pack(side=LEFT,padx=30,pady=20)

buy_upgrade4=Button(root,text=f"{cost4}$+10 Per second", width=20,height=20,command= cps_add_4)
buy_upgrade4.pack(side=LEFT,padx=35,pady=20)

buy_upgrade5=Button(root,text=f"{cost5}$+20 Per second", width=20,height=20,command= cps_add_5)
buy_upgrade5.pack(side=LEFT,padx=37,pady=20)




cps()

root.mainloop()