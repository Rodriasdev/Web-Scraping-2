import requests
from bs4 import BeautifulSoup
import urllib.request

def requestToThePage(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')


    return soup


def captureTags(url):
    soup = requestToThePage(url)

    results = soup.find_all('img')

    count = 0
    for img in results:

        response = requests.get(img['src'])

        formato = img['src'][-4:]

        print(img['src'][-4:])

        with open(f'./img/imagen{str(count)+formato}', 'wb') as f:
            f.write(response.content)

        count = count +1

    





print(captureTags("https://cuevana3i.online/pelicula/"))