#Exercice 1/3: Goal: Get the number of book for each categories.
import requests
import html5lib
from bs4 import BeautifulSoup

test = [1,2,3]
urlList = []
categories = []

url = "https://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html5lib')

target = soup.find('form', class_='form-horizontal').get_text().strip()
targetInt = int(target.split()[0])
print(target)
print(targetInt)