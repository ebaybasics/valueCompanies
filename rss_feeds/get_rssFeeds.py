import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


def get_rss_feeds(url_containing_rss_feeds):

    response = requests.get(url_containing_rss_feeds)
    # Check if the status code indicates success

    if response.status_code != 200:
        return []

    # Use 'lxml' parser if available (usually faster)
    soup = BeautifulSoup(response.text, 'lxml' if 'lxml' in BeautifulSoup.builder_registry.builders else 'html.parser')

    # Initialize an empty set to store unique RSS URLs
    rss_urls = set()

    # Use tqdm to display a progress bar while extracting RSS URLs
    for link in tqdm(soup.find_all('a'), desc='Extracting RSS URLs', unit='link'):
        href = link.get('href')
        if href and 'rss' in href:
            rss_urls.add(href)

    return list(rss_urls)


