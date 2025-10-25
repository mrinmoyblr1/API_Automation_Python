import requests

# cookies
# always send cookie in Dictionary format
cookie = {'visit-month': 'February'}
# We can handle redirection using flag allow_redirects=False
response = requests.get('http://rahulshettyacademy.com/', allow_redirects=False, cookies=cookie, timeout=5)
# response = requests.get('http://rahulshettyacademy.com/', allow_redirects=True, cookies=cookie)
# print(response.history)
print(response.status_code)

# We can incorporate cookies also with session as below
se = requests.session()
se.cookies.update({'visit-Year': '2025'})
# Here we will get two different cookies, once from session object and another from cookies=cookie, passing through parameter
response1 = se.get('https://httpbin.org/cookies', cookies=cookie)
print(response1.text)

print("==========================================================================")
# Attachments
url = "https://petstore.swagger.io/v2/pet/100/uploadImage"

files = {'file': open('test.txt', 'rb')}
# rb stands for opening file in read mode
r = requests.post(url, files=files)
print(r.status_code)
print(r.json())
print(r.text)
