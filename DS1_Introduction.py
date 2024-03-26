import requests
import html5lib
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://books.toscrape.com/"
response = requests.get(url)
titleList = []

soup = BeautifulSoup(response.text, 'html5lib') #Available parser: 'lxml-xml' => Generic / 'html,parser' => Specific html, faster but less flexible with error. / 'html5lib' => Specific html, slower because written in python and not in C.


for li_tag in soup.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3"):
    title = li_tag.find('article', class_="product_pod").find('h3').find('a')
    titleList.append(title.get('title'))


print(titleList)