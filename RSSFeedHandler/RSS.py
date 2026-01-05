import feedparser
class RSSFeed:
    def __init__(self):
        pass
    def get_orders(self):
        def get_orders():
            feed_url = r"https://go.lsgkerala.gov.in/pages/rss.php"
            feed = feedparser.parse(feed_url)
            # for i in feed['entries']:
            # print(i)
            lst = []
            print(feed['entries'])
            for i in feed['entries']:
                lst.append({
                    'title': i['title'],

                })
            return lst