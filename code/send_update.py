from bs4 import BeautifulSoup
from requests import get
import logging
import time
import telebot
from telebot import types
from database_config import *
import mysql.connector
import matplotlib.pyplot as plt
import mysql.connector
from database_config import *

mydb = mysql.connector.connect(
  host=hostname,
  user=username,
  passwd=password,
  database=databasename
)
mycursor = mydb.cursor(buffered=True)
sql = "SELECT * FROM crypto_curr"
mycursor.execute(sql)
ans = mycursor.fetchone()
API_TOKEN = apitoken
bot = telebot.TeleBot(API_TOKEN)
sql = "SELECT * FROM subscription"
mycursor.execute(sql)
row_count = mycursor.rowcount
id = 0
if row_count != 0:
    row = mycursor.fetchone()
    while row is not None:
        str1 = ''
        id = int(row[0], 10)
        if(row[1] == 1):
            str1 = str1+"BTC  "+ans[0]+"\n"
        if(row[2] == 1):
            str1 = str1+"MKR  "+ans[1]+"\n"
        if(row[3] == 1):
            str1 = str1+"THR  "+ans[2]+"\n"
        if(row[4] == 1):
            str1 = str1+"BCH  "+ans[3]+"\n"
        if(row[5] == 1):
            str1 = str1+"XIN  "+ans[4]+"\n"
        if(row[6] == 1):
            str1 = str1+"ETH  "+ans[5]+"\n"
        if(row[7] == 1):
            str1 = str1+"DASH  "+ans[6]+"\n"
        if(row[8] == 1):
            str1 = str1+"BSV  "+ans[7]+"\n"
        if(row[9] == 1):
            str1 = str1+"LTC  "+ans[8]+"\n"
        if(row[10] == 1):
            str1 = str1+"ZEC  "+ans[9]+"\n"
        bot.send_message(id, str1)
        row = mycursor.fetchone()