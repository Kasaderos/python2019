from tkinter import *


TKroot = Tk()
TKroot.title("Hello")
root = Frame(TKroot)
root.place(relx = 0, rely = 0, relwidth = 1)
root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 1)
root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)
btn_Add = Button(root, text="Add")
btn_Add.grid(row=0, column=0, sticky=E+W+S+N)
Exit = Button(root, text="Exit", command=root.quit)
Exit.grid(row=0, column=1, sticky=E+W+S+N)
root.mainloop()

