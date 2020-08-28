#https://www.gamekult.com/jeux/dernieres-sorties.html
#<div class ="pr__game-h__mdb__details">Titre, Editeur, Deveuloper, Genre, Plateforme</div>
#<div class ="pr__game-h__mdb__details">Date de sortie par Plateforme, prix</div>
import requests
from bs4 import BeautifulSoup
import pprint

html = requests.get("https://www.gamekult.com/jeux/dernieres-sorties.html")
html_doc = html.text
soup = BeautifulSoup(html_doc, 'html.parser')
#print(soup.find_all("div",class_="pr__game-h__mdb__details"))

titles = soup.body.find_all("span", class_="pr__game-h__mdb__details__title gk__helpers__fat-title-m")

category = soup.body.find_all("span", class_="pr__game-h__mdb__details__category")



test = soup.find("span", attrs={'class': "pr__game-h__mdb__details__title gk__helpers__fat-title-m"})
result = test.find_all("a")

#qu'un seul titre
print(result)
