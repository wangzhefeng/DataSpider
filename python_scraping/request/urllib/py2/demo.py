#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-23 16:24:55
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

url = "http://www.baidu.com"

response = urlopen(url, data = None, timeout = 10)

# html = html.decode('utf-8')
html = BeautifulSoup(response.read(), 'lxml')

print(html)

