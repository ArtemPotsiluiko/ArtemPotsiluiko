import requests

from bs4 import BeautifulSoup
url = 'http://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
titles = [h3.a['title'] for h3 in soup.find_all('h3')]
for title in titles:
    print(title)