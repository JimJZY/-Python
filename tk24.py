from tkinter import *

OPTIONS = [
    "Califronia",
    "458",
    "FF",
    "ENZO",
    "LaFerrari"
    ]

root = Tk()

variable = StringVar()
variable.set(OPTIONS[0])

w = OptionMenu(root,variable,*OPTIONS)
w.pack()

mainloop()
