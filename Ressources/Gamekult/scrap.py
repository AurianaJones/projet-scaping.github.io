#https://www.gamekult.com/jeux/dernieres-sorties.html
#<div class ="pr__game-h__mdb__details">Titre, Editeur, Deveuloper, Genre, Plateforme</div>
#<div class ="pr__game-h__mdb__offers">Date de sortie par Plateforme, prix</div>
import requests
from bs4 import BeautifulSoup
import pprint

html = requests.get("https://www.gamekult.com/jeux/dernieres-sorties.html")
html_doc = html.text
soup = BeautifulSoup(html_doc, 'html.parser')

#titles = "span", class_="pr__game-h__mdb__details__title"
#category = "span", class_="pr__game-h__mdb__details__category"
#compagny = "span", class_= "pr__game-h__mdb__details__company"
#platform = "span", class_ = "pr__platform__tag--link"


test = soup.find("span", attrs={'class': "pr__game-h__mdb__details__title"})
result = test.find_all("a")

all_game = soup.find_all("div", class_="pr__game-h__mdb__details")
dates_prices_plat = soup.find_all("div" ,class_="pr__game-h__mdb__offers")
print(dates_prices_plat)
