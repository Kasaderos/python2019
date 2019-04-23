from tkinter import *
from tkinter import ttk
import random


def rand_color():
    return "#" + str(random.randint(100000, 999999))


def add_btn():
    color = rand_color()
    stylish = ttk.Style()
    stylish.configure(color + "." + "TButton", background=color)
    btn = ttk.Button(frame2, text="Color", style=color + "." + "TButton")
    lbl = ttk.Label(frame2, text="Color", background=color, anchor="center")
    column, row = frame2.size()
    btn.grid(row=row + 1, column=0, sticky="news")
    lbl.grid(row=row + 1, column=1, sticky="news")
        
    frame.rowconfigure(row+1, weight=1)

root = Tk()
root.title("example03")

frame = ttk.Frame(root)
frame.pack(fill=X)

btn_add = ttk.Button(frame, text="Add", command=add_btn)
btn_exit = ttk.Button(frame, text="Exit", command=root.quit)

btn_add.grid(row=0, column=0, sticky="news")
btn_exit.grid(row=0, column=1, sticky="news")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

frame2 = ttk.Frame(root)
frame2.pack(fill=X)
root.mainloop()
root.destroy()
