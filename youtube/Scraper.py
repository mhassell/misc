#!/usr/bin/python

# https://stackoverflow.com/questions/39061354/scraping-youtube-playlist-video-links

import urllib2
from bs4 import BeautifulSoup
from pytube import YouTube
import MySQLdb

class Scraper(object):

    def __init__(self):
        self.conn = MySQLdb.connect("localhost", config.USERNAME, config.PASSWORD, "computerphile")   # host, uname, pw, dbname
        self.C = self.conn.cursor()

        # constants
        self.nVideos = 5
        self.url = 'https://www.youtube.com/playlist?list=UU9-y-6csu5WGm29I7JiwpnA'
        self.path = '/Users/matthewhassell/Desktop'

    def scrape(self):
        # parse the page here
        htmlParser = "lxml"
        html=urllib2.urlopen(self.url)
        response=html.read()
        soup=BeautifulSoup(response, htmlParser)
        links = soup.find_all('a', attrs={'class':'pl-video-title-link'})
        links = links[0:self.nVideos]   # get the most recent videos

        isOld = [0]*self.nVideos

        self.C.execute("SELECT * FROM videos")
        rows = self.C.fetchall()
        for row in rows:
            print row[1].split('&')[0]

        # check if my most recent fetches are already in the DB
        for j in range(self.nVideos):
            for row in rows:
                if links[j].get("href").split('&')[0] == row[1]:
                    isOld[j] = 1
                    continue

        for j in range(self.nVideos):
            if not isOld[j]:
                yt = YouTube('https://www.youtube.com' + links[j].get("href"))
                self.C.execute("INSERT INTO VIDEOS (url, title) VALUES ('%s', '%s')" % (links[j].get("href").split('&')[0], yt.title))
                self.conn.commit()

        self.C.execute("SELECT * FROM videos")
        rows = self.C.fetchall()
        for row in rows:
            print row[1].split('&')[0]

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

        self.C.close()