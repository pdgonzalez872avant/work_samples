#Better now Pat. How would I go about creating a for loop to create the labels/Frames for frame_data_list below?

# Thanks,

# PG


from tkinter import *

ALL = N+S+W+E


class Application(Frame):
    """Second draft of GUI"""

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)

        button_list = ['Button1',
                       'Button2',
                       'Button3',
                       'Button4',
                       'Button5',
                       ]
        # loop to create the buttons:
        for i, button in enumerate(button_list):
            self.columnconfigure(i+1, weight=1)
            Button(self, text="{0}".format(button)).grid(row=5, column=i+1, sticky=S+W+E)

        # would like to refactor this code as well... for loop should take of some redundancy
        frame_data_list = [('frame1', 'red', 'white'),
                           ('frame2', 'blue', 'white'),
                           ('frame3', 'green', 'white')]

        frame1 = Frame(self, bg='red')
        label_frame1 = Label(self, text='frame1', bg='red', fg='white')
        frame1.grid(row=0, column=0, rowspan=1, columnspan=3, sticky=ALL) #repetitive, must be a better way
        label_frame1.grid(row=0, column=0, rowspan=3, columnspan=3, sticky=ALL) #repetitive must be a better way
        self.rowconfigure(1, weight=1)

        frame2 = Frame(self, bg='blue')
        label_frame2 = Label(self, text='frame2', bg='blue', fg='white')
        frame2.grid(row=3, column=1, rowspan=2, columnspan=3, sticky=ALL) # rowspan=3 goes over the button...
        label_frame2.grid(row=3, column=1, rowspan=2, columnspan=2, sticky=ALL)
        self.rowconfigure(2, weight=1)

        frame3 = Frame(self, bg='green')
        label_frame3 = Label(self, text='frame3', bg='green', fg='white')
        frame3.grid(row=0, column=3, rowspan=5, columnspan=3, sticky=ALL) # rowspan=3 goes over the button...
        label_frame3.grid(row=0, column=3, rowspan=5, columnspan=3, sticky=ALL)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1) #haha, this made it the same height. Interesting. Not sure why!!

root = Tk()
app = Application(master=root)
app.mainloop()