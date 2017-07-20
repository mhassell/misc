# https://stackoverflow.com/questions/39061354/scraping-youtube-playlist-video-links

import urllib2
from bs4 import BeautifulSoup

htmlParser = "lxml"
url='https://www.youtube.com/user/Computerphile/videos'
html=urllib2.urlopen(url)
response=html.read()
soup=BeautifulSoup(response, htmlParser)
links = soup.find_all('a', attrs={'class':'pl-video-title-link'})
for a in links:
    print(a.get("href"))
