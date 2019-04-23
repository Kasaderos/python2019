from tkinter import *
from rgb import Colors
import random

def rand_color(bright=True):
    a, b = "ABCDEF", "0123456"
    return "#"+"".join(random.choice(c)+random.choice(a+b) 
            for c in random.sample(((a,a,a,b,b) if bright else (b,b,b)), 3))

def add_btn():
    def config():
        lbl["background"] = rand_color(False)
        lbl["foreground"] = rand_color(True)
        btn["background"] = rand_color(True)
        btn["foreground"] = rand_color(False)
    #stylish = ttk.Style()
    #stylish.configure(color + "." + "TButton", background=color)
    btn = Button(frame2, text="Color", command=config)
    lbl = Label(frame2, text="Color", anchor="center")
    column, row = frame2.size()
    btn.grid(row=row + 1, column=0, sticky="news")
    lbl.grid(row=row + 1, column=1, sticky="news")
        
    frame2.rowconfigure(row+1, weight=1)
    
root = Tk()
root.title("example03")

frame = Frame(root)
frame.pack(fill=X)

btn_add = Button(frame, text="Add", command=add_btn)
btn_exit = Button(frame, text="Exit", command=root.quit)

btn_add.grid(row=0, column=0, sticky="news")
btn_exit.grid(row=0, column=1, sticky="news")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

frame2 = Frame(root)
frame2.pack(fill=BOTH, expand=1)
frame2.columnconfigure(0, weight=1)
frame2.columnconfigure(1, weight=1) 
root.mainloop()
root.destroy()
