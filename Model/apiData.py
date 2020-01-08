import urllib.request
import json

from Model.fetcher import getResponse

def searchAPI(string):

    # Making an api call that relies on the isbn number
    urlData = "https://www.googleapis.com/books/v1/volumes?q=isbn:"+string.strip()
    jsonData = getResponse(urlData)
    result = jsonData

    if("volumeInfo" in jsonData.keys()):
        # Getting just the volume information for the books
        result = jsonData["volumeInfo"]


    return result
