from bs4 import BeautifulSoup
import urllib.request

def parser_links(urlpage, links, nomdomaine):
    #PARSER RECUPERATION LINKS
    page = urllib.request.urlopen(urlpage)
    soup = BeautifulSoup(page, 'html.parser')

    # On cherche et on append les liens
    table = soup.find('table', attrs={'class': 'table'})
    results = table.find_all('tr')
    for result in results:
        data = result.find_all('td')
        if len(data) == 0:
            continue
        data1 = data[1]
        a = data1.find('a')
        href = a['href']
        links.append(nomdomaine + href)
    print("Nombre d'URL stockées dans notre liste >",len(links))
