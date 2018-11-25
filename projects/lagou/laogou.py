#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wangzhefeng'



import requests
import json

def read_page(url, page_num, keyword):
	headers = {
		'Connection':'keep-alive',
		'Host':'www.lagou.com', 
		'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
	}
	if page_num == 1:
		boo = 'true'
	else:
		boo = 'false'
	page_data = {
		'first':boo,
		'pn':page_num,
		'kd':keyword
	}
	req = requests.post(url = url, headers = headers, data = page_data)
	data = req.text
	return data

def read_tag(page, tag):
	page_json = json.loads(page)
	page_json = page_json['content']['positionResult']['result']
	page_result = [num for num in range(15)]
	for i in range(15):
		page_result[i] = []
		for page_tag in tag:
			page_result[i].append(page_json[i].get(page_tag))
		page_result[i][8] = ",".join(page_result[i][8])
	return page_result


def main():
	url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0"
	page_num = 1
	keyword = "php"
	data = read_page(url, page_num, keyword)
	print(data)

if __name__ == "__main__":
	main()