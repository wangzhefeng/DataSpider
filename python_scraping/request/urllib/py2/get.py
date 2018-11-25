#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-23 17:11:12
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

# GET

values = {}
values['username'] = "Wangzf7"
values['password'] = "wangzf711235813"
# data = urllib.urlencode(values)

url = "http://passport.csdn.net/account/login"
geturl = url + "?" + data
print(geturl)

html = urlopen(geturl)
html = BeautifulSoup(html.read(), 'lxml')
print(html)