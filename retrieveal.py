'''This application is used to pull the name, author, and page numbers
based on a 10-digit isbn number to allow the user to easily find this information
based on the google api'''


import urllib.request
import json

# Built Packages Section
from data.fetcher import getResponse



def main():

    ## TODO Make a GUI that will run on this page
    ## that will allow a value to change the search parameters

    ## TODO create an excel handler or database handler that will put the results into a database to 
    ## Maintain the values for long term storage and to get back the total stats on pages read and stuff

    # Search criteria can be any string 10 digit ISBN number works best so far
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
