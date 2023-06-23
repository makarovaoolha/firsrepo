import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    articles = soup.find_all('h2', class_='article-title')
    for article in articles:
        print(article.text)


url = 'http://example.com'  # Замініть на URL сторінки, яку ви хочете парсити
html = get_html(url)
parse_html(html)
