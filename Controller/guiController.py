from tkinter import messagebox
from Model.apiData import searchAPI
from Model.apiData import searchAPI

def limit(string):
    '''Limiting the string to a certain length in
    this case it is s a length of 13 Called each time the 
    user types into the textBox'''

    try:           
        result = (int(string.get()))

        # Checking that only valid numberic values are used
        if(result > 9999999999999 or result < 0):
            messagebox.showinfo("Invalid Input", "Can only search a 13 digit Number")
            
            # Setting the new value to the first 13 digits for sanitation purposes
            string.set(string.get()[:13])

    except ValueError:
        messagebox.showwarning("Invalid Input", "Only a numeric value is allowed: ")
        string.set("")


def submit(searchMessage):
    '''submit is used to pass the searched information back to main to modify 
    the search api string'''
    
    return searchAPI(searchMessage.strip())




