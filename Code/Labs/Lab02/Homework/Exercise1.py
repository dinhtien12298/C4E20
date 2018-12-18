from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

# Part 1
url = 'https://www.apple.com/itunes/charts/songs/'
html_content = urlopen(url).read().decode('utf-8')

soup = BeautifulSoup(html_content, 'html.parser')
section = soup.find('section','chart-grid')

li_list = section.find_all('li')
data = []
for li in li_list:
    song = {}
    a1 = li.h3.a
    a2 = li.h4.a
    song['Name'] = a1.string
    song['Artist'] = a2.string

    data.append(song)

pyexcel.save_as(records=data, dest_file_name="Itune Top List Song.xls")

# Part 2
for song in data:
    options = {
    'default_search': 'ytsearch',
    }
    dl = YoutubeDL(options)
    dl.download([song['Name']+song['Artist']])