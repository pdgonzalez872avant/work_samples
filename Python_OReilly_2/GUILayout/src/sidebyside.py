from tkinter import *

root = Tk()

w = Label(root, text="Red Label", bg="red", fg="white")
w.pack(side=TOP, fill=BOTH)
#w.pack(side=LEFT)
w = Label(root, text="Green Label", bg="green", fg="black")
w.pack(side=TOP, fill=BOTH, expand=True)
#w.pack(side=LEFT)
w = Label(root, text="Blue Label", bg="blue", fg="white")
w.pack(side=TOP, fill=BOTH, expand=True)
#w.pack(side=LEFT)

mainloop()

