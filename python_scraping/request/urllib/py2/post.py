#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-23 17:10:37
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from urllib.request import urlopen, urlencode
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

# POST
values = {'username': "Wangzf7", 'password': 'wangzf711235813'}
data = urlencode(values)

# values = {}
# values['username'] = "Wangzf7"
# values['password'] = "wangzf711235813"
# data = urllib.urlencode(values)

# print data

url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
html = urlopen(url, data)
html = BeautifulSoup(html.read(), 'lxml')

print(html)