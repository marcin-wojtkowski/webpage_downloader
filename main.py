"""
    Stage 1
        Download a webpage. Save the webpage data on my PC. Store it in a file.
        Have the format be identical to its online format.

"""

import requests
from bs4 import BeautifulSoup


webpage_url = input()

webpage = requests.get(webpage_url)

print(webpage)
#returns Reponse[200] which means success 
