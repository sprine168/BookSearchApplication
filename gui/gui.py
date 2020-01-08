from tkinter import *
from tkinter import ttk



def initGui():

    def submit():
        print(textBox.get())

    gui = Tk()
    
    # Box and Title settings
    gui.title("Search Book Application")
    gui.geometry("500x450")

    # Search Button
    label = Label(gui, text="Enter 10-Digit ISBN number for book Searching")
    label.grid( column = 2, row = 0 )

    # Search TextBox
    textBox = Entry( gui )
    textBox.grid( column = 2, row = 2 )
    textBox.focus()

    # Button to submit
    button = Button( gui, text="Get Results!", command = submit)
    button.grid( column = 3, row = 3 )

    gui.mainloop()
