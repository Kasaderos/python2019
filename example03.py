from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("example03")
frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky="news")

btn_add = ttk.Button(frame, text="Add")
btn_exit = ttk.Button(frame, text="Exit", command=root.quit)

btn_add.grid(row=0, column=0, sticky="news")
btn_exit.grid(row=0, column=1, sticky="news")
root.mainloop()

