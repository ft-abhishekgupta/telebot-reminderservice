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

url = 'https://www.rottentomatoes.com/top/'
response = get(url)
soup = BeautifulSoup(response.text, 'html.parser')
tab = soup.find('ul', attrs={'class': 'genrelist'})
pref = 'https://www.rottentomatoes.com'
for i in tab.find_all('div'):
    l1.append(i.text)
for link in tab.find_all('a'):
    if link.has_attr('href'):
        l2.append(pref+link.attrs['href'])
f = open("auxiliary/MOVIES.txt", "w")
l1 = [x.replace("100", "20") for x in l1]
for i in range(0, len(l1)):
    f.write(l1[i] + "      ")
    f.write(l2[i] + "\n")

for pj in range(0, len(l1)):
    response = get(l2[pj])
    soup = BeautifulSoup(response.text, 'html.parser')
    name = []
    score = []
    x = soup.find_all(attrs={'class': 'unstyled articleLink'})
    for tr in soup.find_all('tr')[1:]:
        tds = tr.find_all('td')
        for i in tds:
            x = i.find(attrs={'class': 'unstyled articleLink'})
            try:
                name.append(x.text)
            except:
                print("", end='')
        for i in tds:
            x = i.find(attrs={'class': 'tMeterScore'})
            try:
                score.append(x.text)
            except:
                print("", end='')
    name = [x.strip('\n   ') for x in name]

    score = [x.strip(" ") for x in score]
    f = open(l1[pj]+" mv"+".txt", "w")
    for i in range(0, len(name)):
        if i == 20:
            break
        f.write(name[i] + "      ")
        f.write(score[i] + "      ")
        url = 'https://www.youtube.com/results?search_query=' + \
            name[i]+" Trailer"
        response = get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        vids = soup.find('a', attrs={'class': 'yt-uix-tile-link'})
        tmp = 'https://www.youtube.com' + vids['href']
        f.write(tmp+"\n")
        print(i)
