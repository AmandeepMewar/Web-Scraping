import pandas as pd
from bs4 import BeautifulSoup
import requests

Q = []
A = []
T = []

for i in range(1,11):
    url = requests.get('https://quotes.toscrape.com/page/{}/'.format(i)).text
    soup = BeautifulSoup(url, 'lxml')
    content = soup.find_all('div', class_="quote")

    for qoutes in content:
        qoute = qoutes.find('span', class_='text').text.replace('"','')
        author = qoutes.find('small', class_='author').text
        tag = qoutes.div.meta['content']

        Q.append(qoute)
        A.append(author)
        T.append(tag)

df = pd.DataFrame({'Quotes': Q, 'Author': A, 'Tags': T})
df.to_excel('output.xlsx')

