'''This application is used to pull the name, author, and page numbers
based on a 10-digit isbn number to allow the user to easily find this information
based on the google api'''

import urllib.request
import json

# Built Packages Section
from data.fetcher import getResponse
from gui.gui import initGui

def main():

    ## TODO put all the values after this for outputting to the GUI

    # Making an api call that relies on the isbn number
    urlData = "https://www.googleapis.com/books/v1/volumes?q=isbn:1910449075"
    jsonData = getResponse(urlData)

    # Getting just the volume information for the books
    result = jsonData["volumeInfo"]

    # Checking if title exists for this book
    if ("title" in result.keys() ):
        print(result["title"], "Title")
    
    # Checking if author exists for this book
    if("authors" in result.keys()):
        print(result["authors"][0], "Author")
    
    # Checking if pageCount exists for this book
    if ("pageCount" in result.keys()):
        print(result["pageCount"], "Pages")


if __name__ == '__main__':
    main()
    initGui()
