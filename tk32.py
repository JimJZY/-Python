from tkinter import *


m1 = PanedWindow()
m1.pack(fill=BOTH,expand=1)

left = Label(m1,text="Left pane")
m1.add(left)

m2 = PanedWindow(orient=VERTICAL)
m1.add(m2)

top = Label(m2,text="top pane")
m2.add(top)

bottom = Label(m2,text="bottom pane")
m2.add(bottom)


mainloop()
