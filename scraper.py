import sqlite3
from sqlite3 import connect
import os
from jeux import Jeux
from create_tables import create_tables
from bs4func import parser_links

def scraper():
  inc = 0
  nomdomaine = 'https://www.gamecash.fr'
  urlpage = nomdomaine + '/prochaines-sorties.html?o=t&s=a'
  links = []

  print('Lancement du script ...')
  try :
    os.remove("scrap_game.db")
  except :
    pass
  conn = connect('scrap_game.db')
  curs = conn.cursor()

  #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  create_tables(curs,conn)
  parser_links(urlpage, links, nomdomaine)

  for link in links :
    inc += 1
    jeux_objet = Jeux(inc, link, links)
    jeux_objet.scraping_data(link)
    jeux_objet.insert_values_db(curs, conn)
    jeux_objet.console_logs()



