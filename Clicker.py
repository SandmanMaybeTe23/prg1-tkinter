from tkinter import *

root = Tk()
root.title("clicker")
root.configure(background="white")
money=0
cps_amount=0
cps_active=False
stopper=False
cost1=10
root.geometry("300x250")


def cps():
    global money
    global cps_amount
    money+=cps_amount
    show_money.configure(text=money)
    root.after(1000,cps)




def cps_add():
    global money
    global cost1
    global cps_amount
    global cps_active
    if cost1<=money:
        money-=cost1
        cost1*=2
        cps_amount+=1
        buy_upgrade.configure(text=f"{cost1}$+1 Per second")
    else:
        print





def clicks():
    global money

    money+=1
    show_money.configure(text=money)


show_money = Label(root,text=money,width=5,height=5, anchor="center",background="white",)
show_money.pack(padx=15,pady=150)


clicker_button=Button(root,text="+1 Per click",width=20, height=20,command=clicks)
clicker_button.pack(side=LEFT,padx=15,pady=20)

buy_upgrade=Button(root,text=f"{cost1}$+1 Per second", width=20,height=20,command=  cps_add)
buy_upgrade.pack(side=LEFT,padx=20,pady=20)

buy_upgrade2=Button(root,text=f"{cost1}$+1 Per second", width=20,height=20,command=  cps_add)
buy_upgrade2.pack(side=LEFT,padx=25,pady=20)

buy_upgrade3=Button(root,text=f"{cost1}$+1 Per second", width=20,height=20,command=  cps_add)
buy_upgrade3.pack(side=LEFT,padx=30,pady=20)

buy_upgrade4=Button(root,text=f"{cost1}$+1 Per second", width=20,height=20,command=  cps_add)
buy_upgrade4.pack(side=LEFT,padx=35,pady=20)

buy_upgrade5=Button(root,text=f"{cost1}$+1 Per second", width=20,height=20,command=  cps_add)
buy_upgrade5.pack(side=LEFT,padx=40,pady=20)


cps()

root.mainloop()