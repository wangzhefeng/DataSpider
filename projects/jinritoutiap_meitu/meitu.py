#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wangzhefeng'

import requests
from urllib.parse import urlencode

from requests.exceptions import RequestException
import json
import re
from hexd import md5
from bs4 import BeautifulSoup
# import pymongo
# from config import *
from multiprocessing import Pool
from json.decode import JSONDecodeError


# client = pymongo.MongoClient(MONGO_URL, connect = False)
# db = client[MONGO_DB]


def get_page_index(offset, keyword):
	data = {
		'offset':offset,
		'format':'json',
		'keyword':keyword,
		'autoload':'true',
		'count':'20',
		'cur_tab':3
	}
	url = 'http://www.toutiao.com/search_content/?' + urlencode(data)
	try:
		response = requests.get(url)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		print('请求索引页出错')
		return None

def parse_page_index(html):
	try:
		data = json.loads(html)
		if data and 'data' in data.keys():
			for item in data.get('data'):
				yield item.get('article_url')
	except JSONDecodeError:
		pass

def get_page_detail(url):
	try:
		response = requests.get(url)

		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		print('请求详情页出错', url)
		return None

def parse_page_detail(html):
	soup = BeautifulSoup(html, 'lxml')
	title = soup.select('title')[0].get_text()
	print(title)
	images_partten = re.compile('var galley = (.*?);', re.S)
	result = re.search(images_partten, html)
	if result:
		data = json.loads(result.group(1))
		if data and 'sub_images' in data.keys():
			sub_images = data.get('sub_images')
			images = [item.get('url') for item in sub_images]
			for image in images: 
				download_image(image)
			return {
				'title':title,
				'url':url,
				'images':image
			}

# def save_to_mongo(result):
# 	if db[MONGO_TABLE].insert(result):
# 		print('存储在Mongo成功', result)
# 		return True
# 	return False


def download_image(url):
	try:
		response = requests.get(url)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		print('请求图片页出错', url)
		return None

def save_image(content):
	file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
	if not os.path.exists(file_path):
		with open(file_path, 'wb') as f:
			f.write(content)
			f.close()

def main(offset):
	html = get_page_index(offset, KEY_WORD)
	for url in parse_page_index(html):
		html = get_page_detail(url)
		if html:
			result = parse_page_detail(html)
			# print(result)
			# if save_to_mongo(result)


if __name__ == '__main__':
	main()
	groups = [x * 20 for x in range(GROUP_START, GROUP_END + 1)]
	pool = Pool()
	pool.map(main, groups)
 
