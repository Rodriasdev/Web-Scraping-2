import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError,Timeout,ConnectionError

formatos_aceptados=['jpg', 'png', 'webp']

def requestToThePage(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')


    return soup


def captureTags(url):
    soup = requestToThePage(url)

    results = soup.find_all('img')

    for i, img in enumerate(results, start=1):
        try:
            response = requests.get(img['src'])

            formato = img['src'][-3:]
            
            if formato in formatos_aceptados:
                with open(f'./img/imagen_{str(i)+'.'+formato}', 'wb') as f:
                    f.write(response.content)
        except HTTPError as e:
            print(e)
        except Timeout as e:
            print(e)
        except ConnectionAbortedError as e:
            print(e)

captureTags("https://cuevana3i.online/pelicula/")