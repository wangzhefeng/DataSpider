#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wangzhefeng'

import requests
from requests import RequestException
import json
import re


def get_one_page(url, headers):
	try:
		response = requests.get(url, headers)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		return None

def main():
	url = "http://maoyan.com/board/4"
	headers = {
		'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
	}
	html = get_one_page(url, headers)
	print(html)

if __name__ == '__main__':
	main()
