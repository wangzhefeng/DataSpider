#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-24 16:54:09
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import requests
import urllib
from urllib import urlopen
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page) + r'/'
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/61.0.3163.79 Chrome/61.0.3163.79 Safari/537.36'
headers = {'User-Agent': user_agent}

# try:
# 	request = urllib2.Request(url, headers = headers)
# 	response = urllib2.urlopen(request)
# 	# print(response.read())
# 	content = response.read().decode('utf-8')
# 	pattern = re.compile('<div.*?clearfix">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?' + 
# 					     'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>', 
# 					     re.S)
# 	items = re.findall(pattern, content)
# 	for item in items:
# 		haveImg = re.search('img', item[3])
# 		if not havImg:
# 			print item[0], item[1], item[2], item[4]
# except urllib2.URLError, e:
# 	if hasattr(e, 'code'):
# 		print e.code
# 	if hasattr(e, 'reason'):
# 		print e.reason


try:
    request = requests.get(url, headers = headers)
    response = urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?"author clearfix">.*?<h2>(.*?)</h2>.*?<div.*?content">.*?<span>(.*?)</span>.*?<i.*?number">(.*?)</i>.*?<i.*?number">(.*?)</i>',
						 re.S)
    items = re.findall(pattern, content)
    print(items) 
    for item in items:
        # haveImg = re.search("img", item[1])
        # if not haveImg:
            print(item[0],item[1],item[2], item[3])
except URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)

