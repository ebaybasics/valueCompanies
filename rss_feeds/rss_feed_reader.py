import feedparser
from operator import itemgetter

def process_rss_feeds(rss_urls, sort_by='date'):
    # Initialize an empty list to store articles
    articles = []

    # Loop through each RSS URL and fetch the feed
    for rss_url in rss_urls:
        feed = feedparser.parse(rss_url)
        publication = feed['feed']['title']

        # Loop through each entry (article) in the feed
        for entry in feed['entries']:
            article_info = {
                'title': entry['title'],
                'description': entry['summary'],
                'link': entry['link'],
                'date': entry['published_parsed'],
                'publication': publication
            }
            articles.append(article_info)

    # Sort the articles based on the specified criteria
    if sort_by == 'date':
        # Sort by date
        articles.sort(key=itemgetter('date'), reverse=True)
    elif sort_by == 'publication':
        # Sort by publication name
        articles.sort(key=itemgetter('publication'))

    return articles

# Example usage
rss_urls = [
    "http://feeds.marketwatch.com/marketwatch/realtimeheadlines/",
    "http://feeds.marketwatch.com/marketwatch/bulletins/",
    # Add more RSS URLs here
]

# Get and sort articles by date (default)
articles_by_date = process_rss_feeds(rss_urls)

# Display the sorted articles
print("Articles sorted by date:")
for article in articles_by_date:
    print(article['title'], "-", article['publication'], "-", article['date'])

