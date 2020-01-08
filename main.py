'''This application is used to pull the name, author, and page numbers
based on a 10-digit isbn number to allow the user to easily find this information
based on the google api'''

import urllib.request
import json

from Model.fetcher import getResponse
from View.gui import initGui

def main():
    print("Application Running")


if __name__ == '__main__':
    main()
    initGui()
