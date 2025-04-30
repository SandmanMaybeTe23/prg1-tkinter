# importing tkinter
import tkinter as tk

# function to run on pressing
# 'ENTER' key from keyboard.
def key_handler_function(event):
    print("You clicked ENTER key in your keyboard")

# main application window
root = tk.Tk()
root.title("GeeksForGeeks")
root.geometry("300x200")


# Binding ENTER key to function
root.bind("<Return>", key_handler_function)

# run the application
root.mainloop()