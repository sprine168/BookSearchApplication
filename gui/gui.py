from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def initGui():

    def limit(string):
        '''Limiting the string to a certain length in
        this case it is s a length of 13'''

        try:           

            result = (int(string.get()))

            # Checking that only valid numberic values are used
            if(result > 9999999999999 or result < 0):
                messagebox.showinfo("Invalid Input", "Can only search a 13 digit Number")
                # Only allowing 13 length places for the input number
                string.set(string.get()[:13])

        except ValueError:
            messagebox.showwarning("Invalid Input", "Only a numeric value is allowed: ")
            string.set("")

    def submit():
        '''submit is used to pass the searched information back to main to modify 
        the search api string'''

        # TODO use this to pass search information back to main
        print(textBox.get())

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
    button = Button(gui, text="Get Results!", command=submit)
    button.grid(column=3, row=2)

    gui.mainloop()
