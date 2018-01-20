#!/usr/bin/python

# https://stackoverflow.com/questions/39061354/scraping-youtube-playlist-video-links

import urllib2
from bs4 import BeautifulSoup
from pytube import YouTube

class Scraper(object):

    def __init__(self, savePath, url, nVideos, listPath):
        

        # constants
        self.nVideos = nVideos
        self.url =  url   # 'https://www.youtube.com/playlist?list=UU9-y-6csu5WGm29I7JiwpnA'
        self.savePath = savePath  # '/home/kernelpanic/Desktop'
        self.listPath = listPath

    def scrape(self):
        # parse the page here
        htmlParser = "lxml"
        html=urllib2.urlopen(self.url)
        response=html.read()
        soup=BeautifulSoup(response, htmlParser)
        links = soup.find_all('a', attrs={'class':'pl-video-title-link'})
        links = links[0:self.nVideos]   # get the most recent videos

        isOld = [0]*self.nVideos

        # check if my most recent fetches are already in the DB
        f = open(self.listPath,'r')
        for line in f:
            line.rstrip('\n')


        for j in range(self.nVideos):
            for row in rows:
                if links[j].get("href").split('&')[0] == row[1]:
                    isOld[j] = 1
                    continue

        for j in range(self.nVideos):
            if not isOld[j]:
                yt = YouTube('https://www.youtube.com' + links[j].get("href"))
                self.C.execute("INSERT INTO VIDEOS (url, title) VALUES ('%s', '%s')" % (links[j].get("href").split('&')[0], yt.title))
                
        # now download the new ones
        for j in range(self.nVideos):
            if not isOld[j]:
                print "Found new video %s" % links[j].text
                yt = YouTube('https://www.youtube.com' + links[j].get("href"))
                video = yt.get('mp4', '360p')
                video.download(self.path)
            else:
                yt = YouTube('https://www.youtube.com' + links[j].get("href"))
                print yt