#Exercice 1/3: Goal: Get the number of book for each categories.
import requests
import html5lib
from bs4 import BeautifulSoup

test = [1,2,3]
urlList = []
categories = []

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html5lib')

navList= soup.find('ul', class_="nav nav-list").find('li').find('ul')

for link in navList.find_all('li'):
    aTag = link.find('a')
    if aTag:
        url = aTag.get('href')
        urlList.append(url)
        text = aTag.get_text().strip()
        categories.append(text)

print(urlList)
    

