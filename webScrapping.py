import requests
from bs4 import BeautifulSoup

li = []

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

    if childSoup.find('div', {'class': 'see-more inline canwrap'}):
        genere = childSoup.find('div', {'class': 'see-more inline canwrap'})
        if genere.a.text == "Documentory":
            print(rowdata[1].a.text)
            print(genere.a.text)
            li.append(rowdata[1].a.text)

print(li)
print(len(li))
