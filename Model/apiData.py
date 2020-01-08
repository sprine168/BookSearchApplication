import urllib.request
import json

from Model.fetcher import getResponse


def searchAPI(string):


    # Making an api call that relies on the isbn number
    urlData = "https://www.googleapis.com/books/v1/volumes?q=isbn:"+string
    print(urlData)
    jsonData = getResponse(urlData)
    print(jsonData)

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

    return result
