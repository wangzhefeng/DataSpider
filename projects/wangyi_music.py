#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests


class Spider():
	def __init__(self):
		self.root_pattern = ''
		self.url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_4001621382?csrf_token='

	def __get_htmls(self, url):
		htmls = requests.get(url)
		print(htmls.status_code)
		return htmls.text

	def run(self):
		self.__get_htmls(self.url)

def main():
	spider = Spider()
	spider.run()



