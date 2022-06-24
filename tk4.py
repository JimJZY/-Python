from tkinter import *

root = Tk()

photo = PhotoImage(file="")
theLabel = Label(root,
                 text = "学 Python\n到 FishC",
                 justify=LEFT,
                 image=photo,
                 compound=CENTER,
                 font=("华康少女",20),
                 fg="white")

theLabel.pack()

mainloop()
