#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wangzhefeng'


# import re
# from urllib.request import urlopen, Request
# from urllib.error import HTTPError, URLError
# import urllib.parse
# import urllib.robotparser
# from bs4 import BeautifulSoup
# from selenium import chromdriver
# import reuqests
# import lxml
# from pyquery import PyQuery as pq
# import pymysql
# import pymongo
# import redis
# import flask
# import django

import re
import requests
import pandas as pd

from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud


f_creationTime = open("creationTime.txt", "a")
# f_discussionId = open("discussionId.txt", "a")
for page in range(0, 10):
	try:
		url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv7732&productId=5089255&score=0&sortType=5&page=' + str(page) + '&pageSize=10&isShadowSku=0&rid=0&fold=1'
		html = requests.get(url)
		response = html.text
		pattern_creationTime = re.compile('"content":"(.*?)","') #"creationTime"
		res_creationTime = re.findall(pattern_creationTime, response)
		# pattern_discussionId = re.compile(r'"content":"(.*?)","discussionId"')
		# res_discussionId = re.findall(pattern_discussionId, response)
		for i in res_creationTime:
			i = i.replace("\\n", "")
			f_creationTime.write(i + '\n')
		# for i in res_discussionId:
		# 	i = i.replace("\\n", "")
		# 	f_discussionId.write(i + '\n')
	except:
		print('The '+ str(page) + 'has a problem!')
		continue
f_creationTime.close()
# f_discussionId.close()


f = open("creationTime.txt", "r")

text = f.read()
cut_text = ' '.join(jieba.lcut(text))
print(cut_text)
color_mask = imread("iphone8_.jpg")
cloud = WordCloud(
	#font_path = 'msyh.ttf',
	background_color = 'white',
	mask = color_mask,
	max_words = 2000,
	max_font_size = 5000
)
word_cloud = cloud.generate(cut_text)
plt.imshow(word_cloud)
plt.axis('off')
plt.show()

f.close()
