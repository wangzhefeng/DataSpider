#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wangzhefeng'


import requests

def baidu_func(url):
	headers = {}
	params = {}
	req = requests.post(url, headers = headers, params = params)
	print(req.text)

if __name__ == '__main__':
	url = "http://openapi.winit.com.cn/openapi/service"
	baidu_func(url)