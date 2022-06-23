from tkinter import *

root = Tk()

textLabel = Label(root,
                  text="您所下载的影片含有未成年人限制内容，\n请满19周岁再点击访问！",
                  justify=LEFT,   #左对齐
                  padx=10,pady=10)
textLabel.pack(side=LEFT)

photo = PhotoImage(file="")
imgLabel = Label(root,image=photo)
imgLabel.pack(side=RIGHT)

mainloop()
