# import libraries
import sqlite3
from sqlite3 import connect
conn = connect('/Users/hugofugeray/Desktop/projet-scaping.github.io/scrap_gamecash/scrap_game.db')
curs= conn.cursor()
from bs4 import BeautifulSoup
import urllib.request
import csv
import numpy as np





curs.execute('''CREATE TABLE IF NOT EXISTS games (
id  INTEGER PRIMARY KEY AUTOINCREMENT,
Plateforme TEXT,
Titre TEXT,
Genre TEXT,
Date_de_sortie TEXT)'''
);
conn.commit()


# specify the url
urlpage = 'https://www.gamecash.fr/prochaines-sorties.html?o=t&s=a'

# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(urlpage)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# find results within table
table = soup.find('table', attrs={'class': 'table'})
results = table.find_all('tr')
print('Number of results', len(results))

# create and write headers to a list
rows = []
rows.append(['PLATEFORME', 'TITRE', 'GENRE', 'DATE DE SORTIE'])
print(rows)


#def insert(Titre, Genre, Plateforme, Date_de_sortie):

# write each result to rows

# loop over results
for result in results:
# find all columns per result

  data = result.find_all('td')
# check that columns have data
  if len(data) == 0:
    continue
# write columns to variables
  Plateforme = data[0].getText()
  Titre = data[2].getText()
  Genre= data[3].getText()
  Date_de_sortie = data[4].getText()
  curs.execute("INSERT INTO games (Titre, Genre, Plateforme, Date_de_sortie) VALUES (?, ?, ?, ?);", (Titre, Genre, Plateforme, Date_de_sortie))

  conn.commit()


  #rows.append([PLATEFORME , TITRE, GENRE, DATE_DE_SORTIE])
  #print(rows)
# Create csv and write rows to output file
#with open('games.csv','w', newline='') as f_output:
 # csv_output = csv.writer(f_output)
 # csv_output.writerows(Plateforme)


