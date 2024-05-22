import requests
from bs4 import BeautifulSoup


def requestToThePage(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')


    return soup


def captureTags(url):
    soup = requestToThePage(url)

    results = soup.find_all('img')

    
    for img in results:
        print(img)


    # labels={

    # }

    # for a in results:

    #     if a['href'][:5] != 'https':
    #         page = requestToThePage(url + a['href'])

    #         res = page.find_all(["h1", "p"])

    #         listOfLabels = []

    #         for label in res:
    #             listOfLabels.append(label)
            
    #         labels[url + a['href']] = listOfLabels







print(captureTags("https://cuevana3i.online/pelicula/"))