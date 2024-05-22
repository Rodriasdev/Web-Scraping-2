import requests
from bs4 import BeautifulSoup

def requestToThePage(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')


    return soup


def captureTags(url):
    soup = requestToThePage(url)

    results = soup.find_all('img')


    for i, img in enumerate(results, start=1):

        response = requests.get(img['src'])

        formato = img['src'][-4:]

        print(img['src'][-4:])

        with open(f'./img/imagen_{str(i)+formato}', 'wb') as f:
            f.write(response.content)


    





print(captureTags("https://cuevana3i.online/pelicula/"))