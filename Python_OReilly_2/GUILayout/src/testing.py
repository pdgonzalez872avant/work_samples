from tkinter import *

ALL = N+S+W+E

class Application(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        
        
        
        for r in range(5):
            self.rowconfigure(r, weight=1)
            Button(self, text="Row {0}".format(r)).grid(row=r, column=0, sticky=ALL)
        
        self.rowconfigure(5, weight=1)
        
        for c in range(5):
            self.columnconfigure(c, weight=1)
            Button(self, text="Col {0}".format(c)).grid(row=5, column=c, sticky=ALL)
        
        f = Frame(self, bg="red")
        f.grid(row=2, column=1, rowspan=3, columnspan=2, sticky=ALL)

        g = Frame(self, bg="blue")
        g.grid(row=0, column=1, rowspan=1, columnspan=2, sticky=ALL)

root = Tk()
app = Application(master=root)
app.mainloop()