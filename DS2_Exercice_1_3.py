#Exercice 1/3: Goal: Get the number of book for each categories.
import requests
import html5lib
from bs4 import BeautifulSoup
import pandas as pd

test = [1,2,3]
urlList = []
categories = []
numberBooks = []

urlMain = "https://books.toscrape.com/"
response = requests.get(urlMain)
soup = BeautifulSoup(response.text, 'html5lib')

navList= soup.find('ul', class_="nav nav-list").find('li').find('ul')

for link in navList.find_all('li'):
    aTag = link.find('a')
    if aTag:
        url = aTag.get('href')
        urlList.append(url)
        text = aTag.get_text().strip()
        categories.append(text)
        childrenPage = requests.get(urlMain + url)
        soupChildren = BeautifulSoup(childrenPage.text, 'html5lib')
        target = soupChildren.find('form', class_='form-horizontal').get_text().strip()
        targetInt = int(target.split()[0])
        numberBooks.append(targetInt)

data = {
    'Categories': categories,
    'Number of Books': numberBooks,
}
df = pd.DataFrame(data)
df['Message'] = ''
df.loc[df['Number of Books'] < 5, 'Message'] = 'Not enough books'
print(df)


    

