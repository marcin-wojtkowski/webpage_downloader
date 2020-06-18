"""
    Stage 1
        Download a webpage. Save the webpage data on my PC. Store it in a file.
        Have the format be identical to its online format.

"""

import requests
from bs4 import BeautifulSoup


webpage_url = input()

webpage = requests.get(webpage_url)

fwebpage_name = webpage_url.replace('/','_') + '.html'

soup = BeautifulSoup(webpage.text, 'lxml')

with open(fwebpage_name, 'w') as f:
    f.write(soup.prettify())
#SUCCESS! Offline parsing is now possible. The entire webpage is saved locally. 
