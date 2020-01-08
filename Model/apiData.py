import urllib.request
import json

# Making an api call that relies on the isbn number
urlData = "https://www.googleapis.com/books/v1/volumes?q=isbn:0198526636"
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
