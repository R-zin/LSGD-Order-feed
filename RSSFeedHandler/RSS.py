import feedparser
class RSSFeed:
    orders = []
    processed_orders = []
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
                'link':i['link'],
                'Summary':i['summary'],
                'Date': i['title'][-10:]
                })
        self.processed_orders = lst
    def get_no_of_orders(self,start=0,num = 8):
        return self.processed_orders[start:num]
    def print_orders(self):
        return self.orders
    def list_par(self):
        print(self.orders.keys())
    def get_len(self):
        return len(self.processed_orders)
