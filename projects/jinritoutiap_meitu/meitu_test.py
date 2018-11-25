#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wangzhefeng'


import re
from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException
from urllib.parse import urlencode
import pymongo

data = {
	'offset':0,
	'format':'json',
	'keyword':'街拍',
	'autoload':'true',
	'count':'20',
	'cur_tab':1
}
url = 'http://www.toutiao.com/search_content/?' + urlencode(data)
response = requests.get(url)
print(response.status_code)
print(response.text)