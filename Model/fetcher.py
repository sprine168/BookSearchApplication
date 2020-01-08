import urllib.request
import json


def getResponse(url):

    jsonData = url

    try:
        operUrl = urllib.request.urlopen(url)

        if(operUrl.getcode() == 200):
            data = operUrl.read()
            jsonData = json.loads(data)

            # Trimming jsonData to first json array searched
            jsonData = jsonData["items"][0]

        else:
            print("Error receiving data", operUrl.getcode())

    except Exception as e:
        print(e)

    return jsonData
