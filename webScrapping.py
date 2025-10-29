import requests
from bs4 import BeautifulSoup

data = requests.get("https://www.imdb.com/find/?s=ep&q=Thriller&ref_=hm_nv_srb_sm/")
soup = BeautifulSoup(data.content, 'html.parser')

# print(soup.prettify())

movieTable = soup.find('table', {'class': 'findList'})

print(movieTable.prettify())

rows = movieTable.findAll('tr')
for row in rows:
    rowdata = row.findAll('td')
    print(rowdata[1].a.text)  # To get title
    subUrl = print(rowdata[2].a['href'])
    subData = requests.get("https://www.imdb.com/" + subUrl)
    childSoup = BeautifulSoup(subData.content, 'html.parser')
    genere = childSoup.find('div', {'class': 'canwrap'})
    print(genere.a.text)
    