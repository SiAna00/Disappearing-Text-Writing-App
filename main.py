from tkinter import *
import threading
import time


def clear():
    global notification_label

    notification_label.config(text="")


def check_if_pressed():
    global notification_label

    if pressed == "no":
        text.delete("1.0", END)
        notification_label.config(text="Hurry up...")

    elif pressed == "yes":
        return


def key_pressed(e):
    global pressed

    pressed = "yes"
    timer.cancel()
    return pressed


def key_released(e):
    global pressed
    global timer

    pressed = "no"
    
    timer = threading.Timer(5.0, check_if_pressed)
    timer.start()

    text.bind("<KeyPress>", key_pressed)


root = Tk()
root.config(padx=60, pady=60, background="floral white")
root.title("The Most Dangerous Writing App")
           
intro_label = Label(root, text="Welcome to the Most Dangerous Writing App", font="Courier 24 bold", background="floral white")
intro_label.grid(column=1, row=0)

notification_label = Label(root, text="", font="Courier 14 bold", background="floral white")
notification_label.grid(column=1, row=2, pady=20)

start_button = Button(root, text="Start", font="Courier 14 bold", background="gray12", foreground="whitesmoke", command=clear)
start_button.grid(column=1, row=3, pady=20, ipadx=15, ipady=5)

text = Text(root, height=30, width=60, font="Courier 14", background="antique white")
text.grid(column=0, row=4, columnspan=3)

text.bind("<KeyRelease>", key_released)


root.mainloop()