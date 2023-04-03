import feedparser
from operator import itemgetter
import get_rssFeeds
import sentiment_analysis
import rss_feeds

def process_rss_feeds(rss_urls, sort_by='date'):
    # Initialize an empty list to store articles
    articles = []
    # Create a progress indicator:
    how_many = len(rss_urls)
    feeds_progressed = 1

    # Loop through each RSS URL and fetch the feed
    for rss_url in rss_urls:
        print(f"{feeds_progressed}/{how_many}")
        try:
            feed = feedparser.parse(rss_url)
            publication = feed['feed']['title']

            # Loop through each entry (article) in the feed
            for entry in feed['entries']:
                try:
                    article_info = {
                        'title': entry['title'],
                        'description': entry['summary'],
                        'link': entry['link'],
                        'date': entry['published_parsed'],
                        'publication': publication
                    }
                    # Ensure the article has a valid date value before appending
                    if article_info['date'] is not None:
                        articles.append(article_info)
                except KeyError as e:
                    # Handle missing 'published_parsed' key or other missing keys
                    print(f"Error processing article in feed '{rss_url}': Missing key {e}")
                    continue
        except Exception as e:
            # Print an error message and continue to the next RSS feed
            print(f"Error processing RSS feed '{rss_url}': {e}")
            continue
        feeds_progressed += 1

    # Sort the articles based on the specified criteria
    if sort_by == 'date':
        # Sort by date
        articles.sort(key=itemgetter('date'), reverse=True)
    elif sort_by == 'publication':
        # Sort by publication name
        articles.sort(key=itemgetter('publication'))

    return articles


# variable linked to rss_feeds.py
general_news_urls = rss_feeds.general_news_urls

# Get Rss feed data from urls provided and create a file named after the rss_feed categories
def get_rss_data(rss_urls=general_news_urls, rss_lst_names='general_news_urls'):
    articles_by_date = process_rss_feeds(rss_urls)
    with open(f'{str(rss_lst_names)}.txt', 'w', encoding='utf-8') as f:
        # Display the sorted articles
        for article in articles_by_date:
            print(article['title'], "-", article['publication'], "-", article['date'])
            f.write(f"{article['title']}\n")
        return f'{str(rss_lst_names)}.txt'




# Running our sent. Analysis. We can now run as many as we want and change the file names to get more specific news for what we are interested in
sentiment_analysis.run_sentiment(get_rss_data(general_news_urls, 'general_news_urls'))