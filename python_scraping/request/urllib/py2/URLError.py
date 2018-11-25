#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-23 19:02:51
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

# import urllib2

# request = urllib2.Request('http://www.xxxxx.com')

# try:
# 	urllib2.urlopen(request)
# except urllib2.URLError, e:
# 	print e.reason

from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

url = 'http://www.xxxxx.com'

try:
    urlopen(url)
except URLError as e:
    print(e.reason)