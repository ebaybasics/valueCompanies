import get_rssFeeds


# feeds_found_on_website = get_rssFeeds.get_rss_feeds('https://www.nasdaq.com/nasdaq-RSS-Feeds')

# General Market News
general_news_urls = [
    "http://feeds.marketwatch.com/marketwatch/realtimeheadlines/",
    "http://feeds.marketwatch.com/marketwatch/bulletins/",
    "https://biztoc.com/feed",
    "https://hnrss.org/frontpage",
    "https://hnrss.org/newest",
    # Add more RSS URLs here
]

nasdaq = [
    "https://www.nasdaq.com/feed/rssoutbound?category=Earnings",

]

seekingAlpha = [
    "https://seekingalpha.com/feed.xml",
    'https://seekingalpha.com/listing/most-popular-articles.xml',
    'https://seekingalpha.com/tag/editors-picks.xml',
]