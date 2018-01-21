import ScraperTxt


listPath ='/home/kernelpanic/Desktop/computerphile.txt'
url = 'https://www.youtube.com/playlist?list=UU9-y-6csu5WGm29I7JiwpnA'
path = '/home/kernelpanic/Desktop/'
nVideos = 5

myScraper = ScraperTxt.Scraper(path, url, nVideos, listPath)

myScraper.scrape()