#下载电影种子爬虫
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import os
import time
import random
import urllib.request
import urllib.parse
import urllib.error
import urllib.request
import urllib.error
import urllib.parse
import requests
import json

#获取资源链接
url = 'https://www.dy2018.com/html/gndy/dyzz/index.html'
#获取网页源代码
html = requests.get(url)
html.encoding = 'gb2312'
html = html.text
#解析网页源代码
soup = BeautifulSoup(html,'html.parser')
#获取电影名称
movie_name = soup.find_all('a',class_='ulink')  
#获取电影链接
movie_link = soup.find_all('a',class_='ulink',href=re.compile(r'/html/gndy/dyzz/\d+/\d+.html'))
#获取电影发布时间
movie_time = soup.find_all('font',class_='date')
#获取电影下载链接
movie_down = soup.find_all('td',style='WORD-WRAP: break-word')
#获取电影简介
movie_intro = soup.find_all('td',style='padding-left:3px')

#将电影信息输出excel
movie_name_list = []
movie_link_list = []
movie_time_list = []
movie_down_list = []
movie_intro_list = []
for i in movie_name:
    movie_name_list.append(i.string)
for i in movie_link:
    movie_link_list.append('https://www.dy2018.com'+i['href'])
for i in movie_time:
    movie_time_list.append(i.string)
for i in movie_down:
    movie_down_list.append(i.a['href'])
for i in movie_intro:
    movie_intro_list.append(i.text)
movie = pd.DataFrame({'movie_name':movie_name_list,'movie_link':movie_link_list,})
movie.to_excel('movie.xlsx',index=False)