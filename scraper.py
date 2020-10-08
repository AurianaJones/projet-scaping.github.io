import sqlite3
from sqlite3 import connect
import os
from jeux import Jeux
from create_tables import create_tables
from bs4func import scraping_append_links

def scraper():
  print('Lancement du scraper ...')
  nomdomaine = 'https://www.gamecash.fr'
  urlpage = nomdomaine + '/prochaines-sorties.html?o=t&s=a'
  links = []

  try :
    os.remove("scrap_game.db")
  except :
    pass
  conn = connect('scrap_game.db')
  curs = conn.cursor()
  #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  create_tables(curs, conn)
  scraping_append_links(urlpage, links, nomdomaine)

  for link in links :
    game = Jeux(link, links)
    game.scraping_data(link)
    game.insert_values_db(curs, conn)
    game.console_logs()
  conn.close()