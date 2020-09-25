# import libraries
import sqlite3
from sqlite3 import connect
conn = connect('scrap_game.db')
curs= conn.cursor()
from bs4 import BeautifulSoup
import urllib.request
import json
import psycopg2

def db(database_name='scrap_game'):
    return psycopg2.connect(database=database_name)

def query_db(query, args=(), one=False):
    cur = db().cursor()
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return (r[0] if r else None) if one else r






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
# rows = []
# rows.append(['PLATEFORME', 'TITRE', 'GENRE', 'DATE DE SORTIE'])
# print(rows)


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


print(data[0])
print(data[0].getText())

print(Plateforme)


# my_query = query_db("select * from majorroadstiger limit %s", (3,))

# json_output = json.dumps(my_query)




def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# connect to the SQlite databases
connection = sqlite3.connect("scrap_game.db")
connection.row_factory = dict_factory
 
cursor = connection.cursor()

# select all the tables from the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
# for each of the bables , select all the records from the table
for table_name in tables:
		# table_name = table_name[0]
		print (table_name['name'])
		    

		conn = sqlite3.connect("scrap_game.db")
		conn.row_factory = dict_factory
		 
		cur1 = conn.cursor()
		 
		cur1.execute("SELECT * FROM "+table_name['name'])
		 
		# fetch all or one we'll go for all.
		 
		results = cur1.fetchall()
		 
		print (results)

		# generate and save JSON files with the table name for each of the database tables
		with open(table_name['name']+'.json', 'a') as the_file:
		    the_file.write(format(results).replace(" u'", "'").replace("'", "\""))

connection.close()