# https://stackoverflow.com/questions/39061354/scraping-youtube-playlist-video-links

import urllib2
from bs4 import BeautifulSoup 
import os
from pytube import YouTube

# parse the page here

htmlParser = "lxml"
url='https://www.youtube.com/playlist?list=UU9-y-6csu5WGm29I7JiwpnA'
path = '/Users/matthewhassell/Desktop'
html=urllib2.urlopen(url)
response=html.read()
soup=BeautifulSoup(response, htmlParser)
links = soup.find_all('a', attrs={'class':'pl-video-title-link'})

links = links[0:5]   # get the 5 most recent videos

# is this even new?
lastVideoFile = open("LastVideos.txt", "rw")
lastFive = lastVideoFile.read()

for line in lastFive
	

(a.get("href"))

yt = YouTube('https://www.youtube.com' + a.get("href"))
video = yt.get('mp4')

video.download('/Users/matthewhassell/Desktop')