#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wangzhefeng'

import re
import json
# from multiprocessing import Pool
import requests
from requests.exceptions import RequestException



def get_one_page(url, headers):
	try:
		response = requests.get(url, headers)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		return None


def parse_one_page(html):
	pattern = re.compile('<dd>.*?board-index.*?(\d+)</i>.*?data-src="(.*?)".*?name"<a+' + 
						 '.*?>(.*?)</a>.*?star">(.*?)</p>.*?integer(.*?)</p>' + 
						 '.*?>(.*?)</a>.*?star">(.*?)</p>.*?fraction(.*?)</i>.*?</dd>', re.S)
	items = re.findall(pattern, html)
	for item in items:
		yield {
			'index': item[0],
			'image': item[1],
			'title': item[2],
			'actor': item[3].strip()[3:],
			'time': item[4].strip()[5:],
			'score': item[5] + item[6]
		}

def write_to_file(content):
	with open('result.txt', 'a', encoding = 'utf-8') as f:
		f.write(json.dumps(content, ensure_ascii = False) + '\n')
		f.close()

def main(offset):
	headers = {
		'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
	}
	url = "http://maoyan.com/board/4?offset=" + str(offset)
	html = get_one_page(url, headers)
	for item in parse_one_page(html):
		print(item)
		write_to_file(item)
	
if __name__ == '__main__':
	for i in range(10):
		main(i * 10)


	# pool = Pool()
	# pool.map(main, [i * 10 for i in range(10)])

