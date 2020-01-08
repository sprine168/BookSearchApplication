from tkinter import messagebox
from Model.apiData import searchAPI
from Model.apiData import searchAPI

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



def submit(searchMessage):
    '''submit is used to pass the searched information back to main to modify 
    the search api string'''
    searchAPI(searchMessage.strip())
