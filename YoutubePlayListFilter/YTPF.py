import re
import urllib.request

class Scraper():

    def __init__(self,site):
        self.site = site

    def scrape(self):

        html = urllib.request.urlopen(self.site)
        html = html.read()
        html = str(html)
        find = re.findall('href=".*?"',html,re.IGNORECASE)
        find = ' '.join(find)
        find = re.findall('".*?"',find,re.IGNORECASE)
        siteplus = self.site + '/'
        for f in find:
            f = f[3:-1]
            f = siteplus + f
            if 'articles' in f:
                print(f)
scraper = Scraper("https://news.google.com/?hl=ru&gl=RU&ceid=RU:ru")
scraper.scrape()
