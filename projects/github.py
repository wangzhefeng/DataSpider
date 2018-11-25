#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wangzhefeng'


import requests

# 执行API调用并存储相应
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code:", r.status_code)

# 将API相应存储在一个变量中
response_dict = r.json()
print(response_dict)
# 处理结果
print(response_dict.keys())