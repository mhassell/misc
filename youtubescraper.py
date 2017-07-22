# https://stackoverflow.com/questions/39061354/scraping-youtube-playlist-video-links

import urllib2
from bs4 import BeautifulSoup 
import os
from pytube import YouTube

nVideos = 5

# parse the page here
htmlParser = "lxml"
url='https://www.youtube.com/playlist?list=UU9-y-6csu5WGm29I7JiwpnA'
path = '/Users/matthewhassell/Desktop'
html=urllib2.urlopen(url)
response=html.read()
soup=BeautifulSoup(response, htmlParser)
links = soup.find_all('a', attrs={'class':'pl-video-title-link'})

links = links[0:nVideos]   # get the most recent videos

# is this even new?
lastVideoFile = open("lastVideos.txt", "r+b")
lastFive = lastVideoFile.read()


if lastFive == '':
	for a in links:
		lastVideoFile.write((a.get("href")))

	lastVideoFile.close()
else:
	# work forward from the old list and backwards from the new list
	for j in range(nVideos):
		if links[nVideos-1-j].get("href") == lastFive[j]:
			break
	# these are the new ones		
	links = links[0:nVideos-j]
	lastFive = links + lastFive[j:]
	
	# take care of the file
	lastVideoFile.seek(0)
	lastVideoFile.write(lastFive)
	lastVideoFile.close()

# now download the new ones
for a in links:
	yt = YouTube('https://www.youtube.com' + a.get("href"))
	video = yt.get('mp4', '360p')
	video.download('/Users/matthewhassell/Desktop')