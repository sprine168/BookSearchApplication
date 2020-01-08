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