import requests
import html5lib
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html5lib') #Available parser: 'lxml-xml' => Generic / 'html,parser' => Specific html, faster but less flexible with error. / 'html5lib' => Specific html, slower because written in python and not in C.
print(soup.prettify())

