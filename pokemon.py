from bs4 import BeautifulSoup
import requests,csv

url = 'https://pokemondb.net/pokedex/all'
x = requests.get(url)    # The web that we want to scrip
y = BeautifulSoup(x.content, 'html.parser')

table = y.find("table", { "id" : "pokedex" })
idList = table.findAll('span', class_='infocard-cell-data')
namaList = table.findAll('a', class_='ent-name')
listId = []
listNama = []
rownew = []

for id in idList:
    listId.append(id.text)
for nama in namaList:
    listNama.append(nama.text)

for i in range(0,len(idList)):
    row = [listNama[i], listId[i]]
    i += 1
    rownew.append(row)

print(rownew)

with open('pokemon.csv', 'w') as csvfile:
    a = csv.writer(csvfile)
    a.writerow(rownew)
csvfile.close()