from tkinter import messagebox, Label, Button, Entry, Tk, StringVar
import keyboard
import time
import random as rd

root = Tk()
root.title("Auto Key")
root.geometry("500x300")

how_often = 10
keyboard_shortcut = ""
when_hack = rd.randint(3, 6)
print(when_hack)

hack_commands = ["Hi. ", "Recently I've gotten into hacking... ", "This app was a prototype for that. ", "Woop woop. ", "I hope you enjoy it......"]

def set_keyboard_shortcut():
    global keyboard_shortcut
    keyboard_shortcut = keyboard_input.get()

def set_how_often():
    global how_often
    global show_value_label
    try:
        how_often = int(how_often_var.get())
        if how_often == 1:
            show_value_label.config(text=f"Every second the keyboard shortcut will run!")
        elif how_often < 1:
            show_value_label.config(text="That's a less then one -_-")
        else:
            show_value_label.config(text=f"Every {how_often} seconds the keyboard shortcut will run!")
    except ValueError:
        show_value_label.config(text=f"Not a number...")

def start():
    global keyboard_shortcut
    global how_often
    global hack_commands
    for i in range(when_hack):
        time.sleep(how_often)
        keyboard.write(keyboard_shortcut)
    for i in hack_commands:
        time.sleep(3)
        keyboard.write(i)
    keyboard.press_and_release('windows')

    time.sleep(0.5)

    keyboard.write('https://aprilfoolslol.bradley-b46.workers.dev')
    time.sleep(0.5)
    keyboard.press_and_release('enter')
how_often_var = StringVar(value=str(how_often))

welcome_label = Label(text="Hello! This is Auto Key!")
welcome_label.pack()

how_often_input = Entry(root, textvariable=how_often_var)
how_often_input.pack()
Label(text="Use the above entry to type how often this keyboard shortcut will run!").pack()

Button(text="Set value", command=set_how_often).pack()

show_value_label = Label(text="Enter a value to see this!")
show_value_label.pack()

keyboard_input = Entry(root, text="")
keyboard_input.pack()
Label(text="Use the above entry to set your keyboard shortcut!").pack()
Button(text="Set keyboard shortcut", command=set_keyboard_shortcut).pack()

Button(text="Finished?", command=start).pack()

root.mainloop()
