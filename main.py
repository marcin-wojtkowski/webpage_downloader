"""
    Stage 1
        Download a webpage. Save the webpage data on my PC. Store it in a file.
        Have the format be identical to its online format.
           
    Stage 2  
        Add PySimpleGUI as a low level UI
"""

import requests
from bs4 import BeautifulSoup
import PySimpleGUI as sg
sg.theme('Topanga')


layout = [  [sg.Text('Url to download: '), sg.InputText(key='-URL-')],
            [sg.Submit()]]

window = sg.Window('URL Downloader', layout)

event, values = window.read()


webpage = requests.get(values['-URL-'])

fwebpage_name = webpage_url.replace('/','_') + '.html'

soup = BeautifulSoup(webpage.text, 'lxml')

with open(fwebpage_name, 'w') as f:
    f.write(soup.prettify())

    
