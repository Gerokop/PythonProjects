import re
from selenium.webdriver.common.action_chains import ActionChains
from random import randrange
import urllib.request
from bs4 import BeautifulSoup
import webbrowser
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Program():

    pls = []

    def __init__(self):
        
        self.driver = webdriver.Chrome()        
        self.flowed = []
        self.filter = []
        url = input('Вставьте ссылку на плейлист: ')
        pl = PlayList(url)
        Program.pls.append(pl)
        YTScraper(url).scrapeandadd()
        print(Program.pls[0].videos)
        self.driver.get(url)
        while True:
            if self.flowed == []:
                self.web()
            elif len(self.flowed) != len(Program.pls[0].videos):
                self.web()
            else:
                self.flowed = []
                self.web()

    def web(self):
        
        repeat = True
        while repeat == True:
            i = randrange(0,Program.pls[0].videos.index(Program.pls[0].videos[-1])+1)
            if Program.pls[0].videos[i] not in self.flowed:
                repeat = False
            else:
                repeat = True
        url = Program.pls[0].videos[i].url
        self.driver.get(url)
        time.sleep(1)
        self.check(url)
        self.flowed.append(Program.pls[0].videos[i])

    def check(self,url):
        
        repeat = True
        while repeat == True:
            time.sleep(0.5)
            code = self.driver.page_source
            code = str(code)
            timecurrent = re.findall('ytp-time-current.*?span',code,re.DOTALL)
            timeduration = re.findall('ytp-time-duration.*?span',code,re.DOTALL)
            timecurrent = re.findall('\d',timecurrent[0])
            timeduration = re.findall('\d',timeduration[0])
            timecurrent = ''.join(timecurrent)
            timeduration = ''.join(timeduration)
            timecurrent = int(timecurrent)
            timeduration = int(timeduration)
            print('\n')
            print(timecurrent)
            print(self.flowed)
            if timecurrent == (timeduration-1) or timecurrent >= timeduration:
                repeat = False
            else:
                repeat = True
        
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
                tag1 = tag1.split('list')
                tag1 = tag1[0] + tag1[-1]
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
        for i in range(0,len(listname)):
            Program.pls[0].videos.append(Video(listname[i],listurl[i]))
                

class PlayList():

    def __init__(self,url):

        self.videos = []

        self.url = url


    def addinpl(self,url):
        pass

prog = Program()

        
                
