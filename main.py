from tkinter import *
import threading


def check_if_pressed():
    if pressed == "no":
        text.delete("1.0", END)

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
root.config(padx=40, pady=40)

text = Text(root, height=30, width=60)
text.grid(column=0, row=3, columnspan=3)

text.bind("<KeyRelease>", key_released)


root.mainloop()