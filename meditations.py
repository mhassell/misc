
from gtts import gTTS
import requests

url = 'http://classics.mit.edu/Antoninus/meditations.mb.txt'
path = '/Users/matthewhassell/Desktop'

text = requests.get(url).text

tts = gTTS(text, lang='en')
filename = path + "/" + 'meditations' + '.mp3'
tts.save(filename)

