import urllib2
from bs4 import BeautifulSoup 
from pytube import YouTube
import MySQLdb
import config

conn = MySQLdb.connect("localhost", config.USERNAME, config.PASSWORD, "computerphile")   # host, uname, pw, dbname
C = conn.cursor()

# constants 
nVideos = 5
url='https://www.youtube.com/playlist?list=UU9-y-6csu5WGm29I7JiwpnA'
path = '/Users/matthewhassell/Desktop'

# parse the page here
htmlParser = "lxml"
html=urllib2.urlopen(url)
response=html.read()
soup=BeautifulSoup(response, htmlParser)
links = soup.find_all('a', attrs={'class':'pl-video-title-link'})
links = links[0:nVideos]   # get the most recent videos

isOld = [0]*nVideos

# C.execute("SELECT * FROM videos")
# rows = C.fetchall()
# for row in rows:
#     print row[1].split('&')[0]

# check if my most recent fetches are already in the DB
for j in range(nVideos):
    for row in rows:
        if links[j].get("href").split('&')[0] == row[1]:
            isOld[j] = 1
            continue

if sum(isOld) == nVideos:
	print "All up to date"
else: 
	for j in range(nVideos):
		if not isOld[j]:
    		C.execute("INSERT INTO VIDEOS (name) VALUES ('%s')" % (links[j].get("href").split('&')[0]))
    		conn.commit()

	# now download the new ones
	for j in range(nVideos):
    	if not isOld[j]:
        	print "Found new video %s" % links[j].text
        	yt = YouTube('https://www.youtube.com' + links[j].get("href"))
        	video = yt.get('mp4', '360p')
        	video.download(path)

C.close()