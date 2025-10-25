import requests
import payLoad
from utilities.configurations import getConfig, getPassword
from utilities.resources import ApiResources

# Add Book
# post() takes url and json as argument
# Here we are keeping url and headers in separately
url = getConfig()['API']['endpoint'] + ApiResources.addBook
headers = {'Content-Type': 'application/json'}
query = 'select * from Books'
# It has mechanism to convert a Dictionary to JSON
addBook_response = requests.post(url, json=payLoad.buildPayloadFromDB(query), headers=headers, )

print(addBook_response.status_code)
print(addBook_response.json())
# Here we are converting response to json format
response_json = addBook_response.json()

print(type(response_json))
bookID = response_json['ID']
print(bookID)

# Delete Book
url2 = getConfig()['API']['endpoint'] + ApiResources.deleteBook
response_deleteBook = requests.post(url2, json={"ID": bookID}, )

print(response_deleteBook.status_code)
assert response_deleteBook.status_code == 200

res_json = response_deleteBook.json()

print(res_json['msg'])

assert res_json['msg'] == "book is successfully deleted"
