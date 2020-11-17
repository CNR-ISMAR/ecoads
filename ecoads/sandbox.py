from urllib.request import urlopen
from bs4 import BeautifulSoup

def imgimport(suffix):

    URL = "https://deims.org/{}".format(suffix)  #provare con alre pagine prima 
    soup = BeautifulSoup(urlopen(URL), "html5lib")
    img = soup.find('div', {"id": "bootstrap-panel--3"}).img['data-lazy'] #funziona ed ha una / davanti 

    return "https://deims.org{}".format(img)