import requests
import feedparser
from bs4 import BeautifulSoup



def get_rss_feeds(url_containing_rss_feeds):
    response = requests.get(url_containing_rss_feeds)
    soup = BeautifulSoup(response.text, 'html.parser')
    rss_urls = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and 'rss' in href:
            rss_urls.append(href)
    return rss_urls

