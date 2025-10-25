import requests
from utilities.configurations import getConfig
from utilities.resources import ApiResources

url = getConfig()['API']['endpoint'] + ApiResources.getBookAuthors
response = requests.get(url, params={'AuthorName': 'MKB'}, )

# print(response.text)
# print(type(response.text))
# dict_response = json.loads(response.text)
# print(type(dict_response))
# print(dict_response[0]['isbn'])


json_response = response.json()  # .json() will directly retrieve the JSON
print(type(json_response))
print(json_response[0]['isbn'])
print(response.status_code)
print(json_response)

assert response.status_code == 200
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

# Retrieve the Book details with ISBN
expectedBook = {
    "book_name": "Learn Appium Automation with Java 8",
    "isbn": "BCR103",
    "aisle": "103"
}
for actualBook in json_response:
    if (actualBook['isbn']) == 'BCR103':
        print(actualBook)
        print(actualBook == expectedBook)
        assert actualBook == expectedBook
        break
