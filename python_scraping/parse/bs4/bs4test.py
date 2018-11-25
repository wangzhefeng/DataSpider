#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2017-05-10 18:42:03
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from urllib.request import urlopen
from bs4 import BeautifulSoup


# Hello world, BeautifulSoup
url_1 = "http://pythonscraping.com/pages/page1.html"
html_1 = urlopen(url_1)
bsObj_1 = BeautifulSoup(html_1.read(), "lxml")
print(bsObj_1)
print(bsObj_1.html)
print(bsObj_1.head) # bsObj.html.head
print(bsObj_1.title)# bsObj.html.title / bsObj.html.head.title
print(bsObj_1.body) # bsObj.html.body
print(bsObj_1.h1)   # bsObj.html.h1 / bsObj.body.h1 / bsObj.html.body.h1
print(bsObj_1.div)  # bsObj.html.div / bsObj.body.div / bsObj.html.body.div

# 
url_2 = 'http://www.pythonscraping.com/pages/warandpeace.html'
html_2 = urlopen(url_2)
bsObj_2 = BeautifulSoup(html_2, "lxml")
nameList = bsObj_2.findAll("span", {"class":"green"})
for name in nameList:
	print(name.get_text())
