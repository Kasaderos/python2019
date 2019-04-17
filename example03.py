from tkinter import *
from tkinter import ttk
import random


def rand_color():
    return "#" + str(random.randint(100000, 999999))


def add_btn():
    color = rand_color()
    stylish = ttk.Style()
    stylish.configure(color + "." + "TButton", background=color)
    btn = ttk.Button(frame, text="Color", style=color + "." + "TButton")
    lbl = ttk.Label(frame, text="Color", background=color)
    column, row = frame.size()
    btn.grid(row=row + 1, column=0)
    lbl.grid(row=row + 1, column=1)


root = Tk()
root.title("example03")

frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky="news")

btn_add = ttk.Button(frame, text="Add", command=add_btn)
btn_exit = ttk.Button(frame, text="Exit", command=root.quit)

btn_add.grid(row=0, column=0, sticky="news")
btn_exit.grid(row=0, column=1, sticky="news")
root.mainloop()
