import re
import urllib.request
from bs4 import BeautifulSoup
import string

class Program():

    pls = []
    unused = []

    def __init__(self):

        url = input('Вставьте ссылку на плейлист: ')
        url = 'https://www.youtube.com/playl\
ist?list=PLGxKKdc3OAhhu2vAPgUHzSTJOYXLBKMf6'
        pl = PlayList(url)
        Program.pls.append(pl)
        
        for i in range(0,100):
            i = str(i)
            for a in list(string.ascii_lowercase):
                Program.unused.append(r'\x'+i)
                Program.unused.append(r'\x'+a+i)
                Program.unused.append(r'\x'+a+a+i)
                Program.unused.append(r'\x'+a+a)
        YTScraper().scrapeandadd(Program.pls[0].url)
        

class Video():

    def __init__(self,name,url):

        self.name = name
        self.url = url

    def __repr__(self):
        return self.name


class YTScraper():

    def __init__(self):
        pass


    def scrapeandadd(self,site):

        html = urllib.request.urlopen(site)
        html = html.read()
        sp = BeautifulSoup(html, 'html.parser')
        for tag in sp.find_all('a'):
            tag = tag.get('href')
            if 'list' in tag and 'accounts' not in tag:
                tag = str(tag)
                tag = 'https://www.youtube.com' + tag
                html = urllib.request.urlopen(tag)
                html = html.read()
                html = str(html)
                html = html.replace(r'\n','')
                for i in Program.unused:
                    if i in html:
                        html = html.replace(i,'')
                find1 = re.findall('<h1.*?h1>',html,re.IGNORECASE)
                print(find1)
                find1 = '\n'.join(find1)
                print(find1)
                find1 = re.findall('">.*?</span>',find1,re.IGNORECASE)
                print(find1)
                find1 = '\n'.join(find1)
                print(find1)
                find1 = re.findall('>.*?<',find1,re.IGNORECASE)
                find1 = ''.join(find1)
                print(find1)
                find1 = find1[1:-1]
                find1 = find1.strip()
                print(tag)
                print(find1)
                Program.pls[0].videos.append(Video(find1,tag))
                print(input())
            else:
                continue
                

class PlayList():

    def __init__(self,url):

        self.videos = []

        self.url = url


    def addinpl(self,url):
        pass

prog = Program()

        
                
