import re
import urllib.request
from bs4 import BeautifulSoup

class Program():

    pls = []
    unused = []

    def __init__(self):

        url = input('Вставьте ссылку на плейлист: ')
        url = 'https://www.youtube.com/playl\
ist?list=PLGxKKdc3OAhhu2vAPgUHzSTJOYXLBKMf6'
        pl = PlayList(url)
        Program.pls.append(pl)
        YTScraper(url).scrapeandadd()
        
        

class Video():

    def __init__(self,name,url):

        self.name = name
        self.url = url

    def __repr__(self):
        return self.name


class YTScraper():

    def __init__(self,site):

        self.site = site


    def scrapeandadd(self):
        
        listname = []
        listurl = []
        html = urllib.request.urlopen(self.site)
        html = html.read()
        sp = BeautifulSoup(html, 'html.parser')
        site = str(sp)
        for tag in sp.find_all('a'):
            tag = tag.get('href')
            if 'list' in tag and 'accounts' not in tag:
                tag = str(tag)
                tag1 = 'https://www.youtube.com' + tag
                listurl.append(tag1)
            else:
                continue
        name = re.findall('t=0s.*?a>',site,re.DOTALL)
        name = ''.join(name)
        name = re.findall(r'\n  .*?\n  ',name,re.DOTALL)
        for i in name:
            i = name.index(i)
            name[i] = name[i][7:-3]
            name[i].strip()
            print(name[i])
            listname.append(name[i])
        listurl = listurl[1:-1]
        print(listurl)
        print('\n')
        print(listname)
                

class PlayList():

    def __init__(self,url):

        self.videos = []

        self.url = url


    def addinpl(self,url):
        pass

prog = Program()

        
                
