import requests
from bs4 import BeautifulSoup

data = requests.get("https://www.imdb.com/find/?s=ep&q=Thriller&ref_=hm_nv_srb_sm/")
soup = BeautifulSoup(data.content, 'html.parser')

# print(soup.prettify())

movieTable = soup.find('table', {'class': 'findList'})

print(movieTable.prettify())

rows = movieTable.findAll('tr')
for row in rows:
    tds = row.findAll('td')
    print(tds)
