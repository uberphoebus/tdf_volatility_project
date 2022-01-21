#Module name : CrawTest.py

from bs4 import BeautifulSoup
import requests
import urllib.request as req

data = req.urlopen("https://www.ytn.co.kr/news/list.php?mcd=0105")
soup = BeautifulSoup(data, 'html.parser')

list = soup.select("#zone1 > div > div.newslist_wrap > div:nth-child(1) > ul > li")


dict= {}
title_list = []
rdate_list = []
for news in list:
    title = news.select_one("a > div.infowrap > span").text
    rdate = news.select_one("a > div.infowrap > div > span.date").text
    #img =  news.select_one("a > div.thumbwrap > div > div > img").attr("href")
    title_list.append(title)
    rdate_list.append(rdate)

dict["title"] = title_list
dict["rdate"] = rdate_list
print(dict)

#dict = { 'title': [37, 84, 79, 80], 'rdate': [100, 46, 76, 94]}

import pandas as pd
df = pd.DataFrame(data=dict )

print(df.head())

import sqlite3
conn = sqlite3.connect("mydb.db")
df.to_sql(name='ytn', con=conn, if_exists='replace')







# from bs4.py import BeautifulSoupClass
# from bs4 import BeautifulSoup.py
# from myfolder.bs4.py import BeautifulSoupClass


