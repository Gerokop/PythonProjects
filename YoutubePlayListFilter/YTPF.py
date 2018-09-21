import re
from random import randrange
import urllib.request
from bs4 import BeautifulSoup
import webbrowser
import time

class Program():

    pls = []

    def __init__(self):
        
        self.flowed = []
        self.filter = []
        url = input('Вставьте ссылку на плейлист: ')
        pl = PlayList(url)
        Program.pls.append(pl)
        YTScraper(url).scrapeandadd()
        print(Program.pls[0].videos)
        while True:
            if self.flowed == []:
                self.web()
            elif self.flowed.index(self.flowed[-1]) != Program.pls[0].videos\
                   .index(Program.pls[0].videos[-1]):
                self.web()
            else:
                self.flowed = []

    def web(self):
        
        repeat = True
        while repeat == True:
            i = randrange(0,Program.pls[0].videos.index(Program.pls[0].videos[-1])+1)
            if Program.pls[0].videos[i] not in self.flowed:
                repeat = False
            else:
                repeat = True
        print(Program.pls[0].videos[i].url)
        url = Program.pls[0].videos[i].url
        html = urllib.request(url)
        html = html.read()
        site = str(html)
        print(site)
        t = re.findall('',site,re.DOTALL)

    def kok(self):
        webbrowser.open_new_tab(Program.pls[0].videos[i].url)
        self.flowed.append(Program.pls[0].videos[i].url)

            

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
            listname.append(name[i])
        listurl = listurl[1:-1]
        for i in range(0,listname.index(listname[-1])):
            Program.pls[0].videos.append(Video(listname[i],listurl[i]))
                

class PlayList():

    def __init__(self,url):

        self.videos = []

        self.url = url


    def addinpl(self,url):
        pass

prog = Program()

        
                
