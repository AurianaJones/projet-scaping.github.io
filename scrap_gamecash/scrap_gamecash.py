# import libraries
from bs4 import BeautifulSoup
import urllib.request
import csv

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


