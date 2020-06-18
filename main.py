"""
    Stage 1
        Download a webpage. Save the webpage data on my PC. Store it in a file.
        Have the format be identical to its online format.

"""

import requests
from bs4 import BeautifulSoup


webpage_url = input()

webpage = requests.get(webpage_url)

soup = BeautifulSoup(webpage.text, 'lxml')

print(soup)
#returns a messy text including all html tags 
