import re
import urllib.request

class Program():

    pls = []

    def __init__(self):

        url = input('Вставьте ссылку на плейлист: ')

        url = 'https://www.youtube.com/playl\
ist?list=PLGxKKdc3OAhhu2vAPgUHzSTJOYXLBKMf6'

        pl = PlayList(url)

        Program.pls.append(pl)

        YTScraper().scrapeandadd(Program.pls[0].url)
        

class Video():

    def __init__(self,url):

        self.url = url
        html = urllib.request.urlopen(self.url)
        html = html.read()
        html = str(html)
        print(html)
        find = re.findall('<h1.*?h1>',html,re.IGNORECASE)
        print(find)
        find = '\n'.join(find)
        find = re.findall('<yt.*?string>',find,re.IGNORECASE)
        print(find)
        find = '\n'.join(find)
        find = re.findall('>.*?<',find,re.IGNORECASE)
        print(find)
        self.name = find[0][1:-1]

    def __repr__(self):
        return self.name


class YTScraper():

    def __init__(self):
        pass


    def scrapeandadd(self,site):

        html = urllib.request.urlopen(site)
        html = html.read()
        html = str(html)
        find = re.findall('href=".*?"',html,re.IGNORECASE)
        find = ' '.join(find)
        find = re.findall('".*?"',find,re.IGNORECASE)
        for f in find:
            if 'list' in f:
                siteplus = site + '/'
                f = f[3:-1]
                f = siteplus + f
                Program.pls[0].videos.append(Video(f))
                

class PlayList():

    def __init__(self,url):

        self.videos = []

        self.url = url


    def addinpl(self,url):
        pass

prog = Program()

        
                
