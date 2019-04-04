from tkinter import *

def back():
    root.quit()

root = Tk()
btn1 = Button(root, text='quit', width=25, height=5, bg='black', fg='red', command=back)
btn1.grid()
root.mainloop()
