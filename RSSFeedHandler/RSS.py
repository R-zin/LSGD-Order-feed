import feedparser
class RSSFeed:
    orders = []
    def __init__(self):
        self.get_orders()

    def get_orders(self):
        feed_url = r"https://go.lsgkerala.gov.in/pages/rss.php"
        feed = feedparser.parse(feed_url)
        self.orders = feed['entries']
        lst = []
        for i in feed['entries']:
            lst.append({
                'title': i['title'],

                })
        return lst



    def print_orders(self):
        return self.orders

    def list_par(self):
        print(self.orders.keys())
