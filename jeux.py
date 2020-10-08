import sqlite3
from bs4 import BeautifulSoup
import urllib.request


class Jeux :
  game_id = 0
  titre_precedent = ""

  def __init__(self, inc, link, links) :
    self.titre = "Null"
    self.genre = "Null"
    self.prix = "Null"
    self.plateforme = "Null"
    self.date_de_sortie = "Null"
    self.editeur = "Null"
    self.description = "Null"
    print("---------------------------------------------------------------------------------------------\n>>>>>>> Link",inc,"/",len(links)," >",link,"\n")


  def insert_values_db(self, curs, conn) :
    if Jeux.titre_precedent != self.titre :
      Jeux.game_id += 1
      curs.execute("INSERT INTO games (id, title, type, price, release_date) VALUES (?, ?, ?, ?, ?);", (Jeux.game_id, self.titre, self.genre, self.prix, self.date_de_sortie))
      curs.execute("INSERT INTO games_details (game_id, publisher, description) VALUES (?, ?, ?);", (Jeux.game_id, self.editeur, self.description))
    curs.execute("INSERT INTO release_details (game_id, platform) VALUES (?, ?);", (Jeux.game_id, self.plateforme))
    conn.commit()
    Jeux.titre_precedent = self.titre

  def console_logs(self) :
    print("Game_ID >",Jeux.game_id,"\nTitre >",self.titre,"\nGenre >",self.genre,"\nPrix >",self.prix,"\nPlateforme >",self.plateforme,"\nDate de sortie >",self.date_de_sortie,"\nEditeur >",self.editeur,"\nDescription >",self.description)




  def scraping_data(self, link) :
    pagelink = urllib.request.urlopen(link)
    soup2 = BeautifulSoup(pagelink, 'html.parser')


    scrap_price = soup2.find('meta', attrs={'itemprop': 'price'})
    self.prix = scrap_price['content']
    
    scrap_title = soup2.find('h1', attrs={'itemprop': 'name'})
    titre = scrap_title.text
    self.titre = titre.strip()

    scrap_desc = soup2.find('div', attrs={'itemprop': 'description'})
    try :
      description = scrap_desc.text
      self.description = description.strip()
    except :
      self.description = "Null"
      pass

    table2 = soup2.find_all('ul')
    table2_3 = table2[3]
    i = -1
    for ahah in table2_3 :
      i += 1
      if len(ahah) == 4 :
        sPaN = ahah.find('span', attrs={'class': 'value'})
        sPaN = sPaN.text
      if i == 0 :
        self.plateforme = sPaN
      elif i == 2:
        self.genre = sPaN
      elif i == 4 :
        self.editeur = sPaN
      elif i == 6 :
        if len(sPaN) == 10 :
          self.date_de_sortie = sPaN
      elif i == 10 :
        if len(sPaN) == 10 :
          self.date_de_sortie = sPaN
      elif i == 12 :
        self.date_de_sortie = sPaN
    if len(self.date_de_sortie) != 10 :
      self.date_de_sortie = "Null"