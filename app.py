import requests
from bs4 import BeautifulSoup

def requestToThePage(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')


    return soup