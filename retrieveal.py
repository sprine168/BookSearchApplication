import urllib.request
import json


def getResponse(url):

    try:
        operUrl = urllib.request.urlopen(url)

        if(operUrl.getcode()==200):
            data = operUrl.read()
            jsonData = json.loads(data)

            # Trimming jsonData to first json value searched
            jsonData = jsonData["items"][0]

        else:
            print("Error receiving data", operUrl.getcode())

    except Exception as e:
        print(e)

    return jsonData

def main():

    ## TODO Make a GUI that will run on this page
    ## that will allow a value to change the search parameters

    ## TODO create an excel handler or database handler that will put the results into a database to 
    ## Maintain the values for long term storage and to get back the total stats on pages read and stuff

    urlData = "https://www.googleapis.com/books/v1/volumes?q=regrettingyou"
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
