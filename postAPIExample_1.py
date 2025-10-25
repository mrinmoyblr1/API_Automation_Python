import requests
import payLoad
from utilities.configurations import getConfig, getPassword
from utilities.resources import ApiResources

# Add Book
# post() takes url and json as argument
# Here we are keeping url and headers in separately
url = getConfig()['API']['endpoint'] + ApiResources.addBook
headers = {'Content-Type': 'application/json'}
addBook_response = requests.post(url, json=payLoad.addBookPayload("BCR401"), headers=headers, )

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

# Authentication
url2 = 'https://api.github.com/user'
github_response = requests.get(url2, auth=("mrinmoy.blr@gmail.com", getPassword()))
# We can  ignore SSL Certificate error using verify=False
# github_response = requests.get(url2, verify=False, auth=("mrinmoy.blr@gmail.com", getPassword()))
print(getPassword())
print(github_response.status_code)

# File Uploading
url3 = 'https://httpbin.org/post'
files = {'file': open('test.txt', 'rb')}
r = requests.post(url3, files=files)
print(r.status_code)
print(r.json())
print(r.text)

