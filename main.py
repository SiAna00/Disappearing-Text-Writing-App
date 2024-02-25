from tkinter import *
import threading

def create_text_field():
    global text
    text = Text(root, height=30, width=60)
    text.grid(column=0, row=3, columnspan=3)

    text.bind("<KeyRelease>", key_released)


def check_if_pressed():
    if pressed == "no":
        text.destroy()

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

start_button = Button(root, text="Start", command=create_text_field)
start_button.grid(column=1, row=1, padx=10, pady=10)


root.mainloop()