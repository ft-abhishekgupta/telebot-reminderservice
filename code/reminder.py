from bs4 import BeautifulSoup
from requests import get
import logging
import time
import telebot
from telebot import types
import datetime
import mysql.connector
import re
from database_config import *

API_TOKEN = apitoken
bot = telebot.TeleBot(API_TOKEN)
i = []
while 1:
    mydb = mysql.connector.connect(
        host=hostname,
        user=username,
        passwd=password,
        database=databasename
    )
    now = str(datetime.datetime.now())
    print(now)
    cursor = mydb.cursor()
    query = ("SELECT chatId,message FROM reminders WHERE date=%s AND time=%s")
    val = (now[:10], now[11:16])
    print(now[:10])
    print(now[11:16])
    cursor.execute(query, val)
    resultSet = cursor.fetchall()
    for i in resultSet:
        bot.send_message(i[0], i[1])
    time.sleep(60)
