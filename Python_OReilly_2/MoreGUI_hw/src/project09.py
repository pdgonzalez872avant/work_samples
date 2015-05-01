from tkinter import *
from tkinter.filedialog import LoadFileDialog
import os

ALL = N+S+W+E

class Application(Frame):
    """Project 9"""

    def open_file(self):
        entry_frame3_text = self.entry_frame3.get()
        current_directory = str(os.getcwd())
        fpath = str(current_directory + '\\' + entry_frame3_text)
        if os.path.isfile(fpath):
            self.text_frame3.insert(END, open(fpath).read())  # had to use.pack() in a different line for this to work.
        else:
            self.text_frame3.insert(END, 'Sorry, no file in this directory')

# retired handler, doesn't work well
    # def click_handler(self, event):
    #     caller = str(event.widget)
    #     print("clicked", caller, "at", event.x, event.y)  # clicked .53367416.53367360 at 25 7
    #     #print("clicked", "at", event.x, event.y) #  this works so so

    def click_handler(self, event, obj):  # http://stackoverflow.com/questions/4299145/getting-the-widget-that-triggered-an-event
        print("you clicked on", obj, 'at', event.x, event.y)

    def change_text_color(self, button_color):
    #def change_text_color(self, color):
        self.text_frame3.config(foreground=button_color)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)

        # would like to refactor this code as well... for loop should take of some redundancy
        frame_data_list = [('frame1', 'red', 'white'),
                           ('frame2', 'blue', 'white'),
                           ('frame3', 'green', 'white')]

        #will tackle this with pack(), think it is more efficient to place buttons on top/side, etc.
        frame1 = Frame(self, bg='red')
        label_frame1 = Label(self, text='frame1', bg='red', fg='white')

        frame1.grid(row=0, column=0, rowspan=3, columnspan=3, sticky=ALL)  # repetitive, must be a better way
        label_frame1.grid(row=0, column=0, rowspan=3, columnspan=3, sticky=ALL) #repetitive must be a better way


        # Change the obj name to a string, only way I was able to pass the frame name.
        label_frame1.bind("<Button-1>", lambda event, obj='frame1': self.click_handler(event, obj))  # you clicked on .53576480.53576424
        # old one, did not work...
        #label_frame1.bind("<Button-1>", self.click_handler)  # "you clicked on .53576480.53576424"
        self.rowconfigure(1, weight=1)

        frame2 = Frame(self, bg='blue')
        label_frame2 = Label(self, text='frame2', bg='blue', fg='white')

        frame2.grid(row=3, column=1, rowspan=2, columnspan=2, sticky=ALL)  # rowspan=3 goes over the button...
        label_frame2.grid(row=3, column=1, rowspan=2, columnspan=2, sticky=ALL)

        label_frame2.bind("<Button-1>", lambda event, obj='frame2': self.click_handler(event, obj))
        self.rowconfigure(2, weight=1)

        frame3 = Frame(self, bg='green')
        frame3.grid(row=0, column=3, rowspan=5,columnspan=3, sticky=ALL)

        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        #use pack not to mess up with grid and positioning inside the frame.
        #this works, but looks kind of bad when starting the app - looks horrible actually.
        #pretty annoying to work on this layout... So many configs (row and column) that are hard to diagnose.

        self.entry_frame3 = Entry(frame3)
        self.entry_frame3.pack(side="top", fill=X)  # fill: fill style "xy": must be none, x, y, or both
        self.text_frame3 = Text(frame3, height=1, width=1)
        self.text_frame3.pack(side="top", expand=True, fill="both")  # expand = True or False (default)

        # Working on buttons and the bindings
        button_red = Button(self, text="Red")
        button_red.grid(row=5, column=1, sticky=S+W+E)
        button_red.config(command=lambda: self.change_text_color('red'))
        self.columnconfigure(1, weight=1)

        button_blue = Button(self, text="Blue")
        button_blue.grid(row=5, column=2, sticky=S+W+E)
        button_blue.config(command=lambda: self.change_text_color('blue'))
        self.columnconfigure(2, weight=1)

        button_green = Button(self, text="Green")
        button_green.grid(row=5, column=3, sticky=S+W+E)
        button_green.config(command=lambda: self.change_text_color('green'))
        self.columnconfigure(3, weight=1)

        button_black = Button(self, text="Black")
        button_black.grid(row=5, column=4, sticky=S+W+E)
        button_black.config(command=lambda: self.change_text_color('black'))
        self.columnconfigure(4, weight=1)

        button_open = Button(self, text="Open")
        button_open.grid(row=5, column=5, sticky=S+W+E)
        button_open.config(command=self.open_file)

        self.columnconfigure(5, weight=1)

root = Tk()
app = Application(master=root)
app.mainloop()