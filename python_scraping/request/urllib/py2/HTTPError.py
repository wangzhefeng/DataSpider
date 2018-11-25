#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-23 19:05:31
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup


url = 'http://blog.csdn.net/cqcre'

try:
	urlopen(url)
except HTTPError as e:
	print(e.code) 
	print(e.reason) 


try:
	urlopen(url)
except HTTPError as e:
	print(e.code) 
except URLError as e:
	print(e.reason)
else:
	print("OK")


try:
	urlopen(url)
except URLError as e:
	if hasattr(e, "reason"):
		print(e.reason) 
else:
	print("OK") 