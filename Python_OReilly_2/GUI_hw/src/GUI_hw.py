from tkinter import *


class Application(Frame):
    """Application main window class."""
    def __init__(self, master=None):
        """Main frame initialization (mostly delegated)"""
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        """Add all the widgets to the main frame."""
        top_frame = Frame(self)

        self.text_in_1 = Entry(top_frame)
        self.text_in_1.pack()

        self.text_in_2 = Entry(top_frame)
        self.text_in_2.pack()

        self.label = Label(top_frame, text="Enter values above")
        self.label.pack()

        top_frame.pack(side=TOP)

        bottom_frame = Frame(self)
        bottom_frame.pack(side=TOP)

        self.handleb = Button(bottom_frame, text="Convert to Float", command=self.handle)
        self.handleb.pack(side=LEFT)

# Write a GUI-based program that provides two Entry fields, a button and a label. When the button is clicked, the value
# of each Entry should (if possible) be converted into a float. If both conversions succeed, the label should change to
# the sum of the two numbers. Otherwise it should read "***ERROR***."

    def handle(self):
        """Handler"""

        # Wonder how I could implement this here
        # if condition:
        #     B.config(state='normal')
        # else:
        #     B.config(state='disabled')

        empty_fields = ('', '')

        try:
            value1 = float(self.text_in_1.get())
            value2 = float(self.text_in_2.get())

        except ValueError:
            output = "***ERROR - ValueError***"

        try:
            if (value1, value2) != empty_fields:
                output = float(value1 + value2)

            elif (value1, value2) == empty_fields:  #this doesn't work
                output = "empty fields"             #this doesn't work

            else:
                output = "***ERROR***"

        except UnboundLocalError:
            output = "***ERROR - UnboundLocalError***"

        self.label.config(text=output)

root = Tk()
app = Application(master=root)
app.mainloop()

# Failed tests:
    # "empty fields" doesn't work, logic never gets there
    # start app, input both values, click, ok
        #but: with open app with both values input, remove value2, fails

#Question:
# Is there anywhere/somewhere/tool where I can see the logic flow? Somewhat like a pinball machine type of deal?