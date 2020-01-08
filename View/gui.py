from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Controller.guiController import limit
from Controller.guiController import submit 

def initGui():

    def search():
        '''submit is used to pass the searched information back to main to modify 
        the search api string'''
        result = submit(searchMessage.get())  
        updateGui(result)
        
    def updateGui(values):

        # Checking if title exists for this book
        if ("title" in values.keys()):
            print(values["title"], "Title")

        # Checking if author exists for this book
        if("authors" in values.keys()):
            print(values["authors"][0], "Author")

        # Checking if pageCount exists for this book
        if ("pageCount" in values.keys()):
            print(values["pageCount"], "Pages")

    
    gui = Tk()

    # Getting the search message while the user is typing
    searchMessage = StringVar()
    searchMessage.trace("w", lambda name, index, mode,
                        searchMessage=searchMessage: limit(searchMessage))

    # Box and Title settings
    gui.title("Search Book Application")
    gui.geometry("500x450")

    # Search Button
    label = Label(
        gui, text="Enter 10 or 13 digit (w/out spacing, or dashes)\nISBN number for book Searching")
    label.grid(column=2, row=0)

    # Search TextBox
    textBox = Entry(gui, textvariable=searchMessage)
    textBox.grid(column=2, row=2)
    textBox.focus()

    # Button to submit
    button = Button(gui, text="Get Results!", command=search)
    button.grid(column=3, row=2)

    gui.mainloop()
