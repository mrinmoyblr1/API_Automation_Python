import requests
from bs4 import BeautifulSoup

data = requests.get("https://rahulshettyacademy.com/AutomationPractice/")
soup = BeautifulSoup(data.content, 'html.parser')

appium = soup.find("a", string='Appium')
# It's like visible Text
# This will find a tab name with a then it will find which has name as Appium'

appium = appium['href']
print(appium)
