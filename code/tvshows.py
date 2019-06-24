import matplotlib.pyplot as plt
from requests import get
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
from requests import get
import logging
import time
import telebot
from telebot import types
import datetime
import mysql.connector
import mysql.connector
l1 = []
l2 = []
l3 = []
l4 = []
dict1 = {}
dict2 = {}
dict3 = {}
url = 'https://www.imdb.com/feature/genre/'
response = get(url)
soup = BeautifulSoup(response.text, 'html.parser')
x = soup.find_all(attrs={'class': 'table-cell primary'})
for i in x:
    l3.append(i.a.text)
    i = i.find('a')
    if i.has_attr('href'):
        l4.append(i.attrs['href'])
print(l4[24])
f = open("auxiliary/TV_SHOWS.txt", "w")
for i in range(0, len(l3)):
    f.write(l3[i] + "      ")
    f.write(l4[i] + "\n")
        
l3 = [x.strip('\n   ') for x in l3]
print(l3)

for pj in range(0, 24):
    val1 = l4[24+pj]
    response = get('https://www.imdb.com'+val1)
    soup = BeautifulSoup(response.text, 'html.parser')
    x = soup.find_all(attrs={'class': 'lister-item-header'})
    y = soup.find_all(attrs={'class': 'inline-block ratings-imdb-rating'})
    name = []
    score = []
    for i in y:
        score.append(i.strong.text)
    for i in x:
        name.append(i.a.text)
    name = [x.strip('\n   ') for x in name]
    print(str(len(name))+" "+str(len(score)))
    f = open(str(l3[pj])+" tv"+".txt", "w")
    for pj1 in range(0, len(score)):
        print(pj1)
        url = 'https://www.youtube.com/results?search_query=' + \
            str(name[pj1])+" Trailer"
        response = get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        vids = soup.find('a', attrs={'class': 'yt-uix-tile-link'})
        tmp = 'https://www.youtube.com' + vids['href']
        f.write(name[pj1] + "      ")
        f.write(score[pj1] + "      ")
        f.write(tmp+"\n")
