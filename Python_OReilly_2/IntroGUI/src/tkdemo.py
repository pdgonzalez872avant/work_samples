from tkinter import *

class Application(Frame):
    def say_hi(self):
        print('Hi there, everyone!')
    
    def createWidgets(self):
        #self.hi_there = Button(self, text="Hello", fg="blue", bg='yellow' ,command=None)
        self.hi_there = Button(self, text="Hello", fg="blue", bg='yellow' ,command=self.say_hi)
        self.hi_there.pack({"side": "left"})
        
        self.QUIT = Button(self, text="Goodbye", fg="red", command=self.quit)
        self.QUIT.pack({"side": "left"})
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
root = Tk()
app = Application(master=root)
app.mainloop()
        
        
        
        

