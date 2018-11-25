#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-23 18:12:57
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'
html = urlopen(url, timeout = 10)
html = BeautifulSoup(html.read(), 'lxml')
print(html)