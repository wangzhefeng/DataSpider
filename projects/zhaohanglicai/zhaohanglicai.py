#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wangzhefeng'

import re
import requests
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

# 设置请求头
headers = {
	'Accept':'*/*',
	'Accept-Encoding':'gzip, deflate',
	'Accept-Language':'en-US,en;q=0.8',
	'Connection':'keep-alive',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

pageIndex = list(range(1, 57))
print(pageIndex)

# 拼接URL
url_phase1 = "http://www.cmbchina.com/cfweb/svrajax/product.ashx?op=search&type=m&pageindex="
url_phase2 = "&salestatus=&baoben=&currency=&term=&keyword=&series=01&risk=&city=&date=&pagesize=20&orderby=ord1&t=0.13613849132006206"

urls = []
for i in pageIndex:
	urls.append(url_phase1 + str(i) + url_phase2)
print(urls)

# 构造空列表，用于后面的数据存储
Finacing = []

# 通过for循环完成URL的遍历
for url in urls:
	# 获取源代码
	response = requests.get(url, headers = headers).text
	print(response)
	# 正则表达式完成信息的获取
	ProdCode = re.findall('ProdCode:"(.*?)",', response)
	PrdCode = re.findall('PrdCode:"(.*?)",', response)
	PrdName = re.findall('PrdName:"(.*?)",', response)
	TypeCode = re.findall('TypeCode:"(.*?)",', response)
	AreaCode = re.findall('AreaCode:"(.*?)",', response)
	Currency = re.findall('Currency:"(.*?)",', response)
	BeginDate = re.findall('BeginDate:"(.*?)",', response)
	EndDate = re.findall('EndDate:"(.*?)",', response)
	ExpireDate = re.findall('ExpireDate:"(.*?)",', response)
	Status = re.findall('Status:"(.*?)",', response)
	NetValue = re.findall('NetValue:"(.*?)",', response)
	IsNewFlag = re.findall('IsNewFlag:"(.*?)",', response)
	Term = re.findall('Term:"(.*?)",', response)
	Style = re.findall('Style:"(.*?)",', response)
	InitMoney = re.findall('InitMoney:"(.*?)",', response)
	IncresingMoney = re.findall('IncresingMoney:"(.*?)",', response)
	Risk = re.findall('Risk:"(.*?)",', response)
	FinDate = re.findall('FinDate:"(.*?)",', response)
	SaleChannel = re.findall('SaleChannel:"(.*?)",', response)
	SaleChannelName = re.findall('SaleChannelName:"(.*?)",', response)
	IsCanBuy = re.findall('IsCanBuy:"(.*?)"}', response)
	# 数据存储到字典中
	Finacing.append({
		'PrdCode': PrdCode,
		'PrdName': PrdName,
		'TypeCode': TypeCode,
		'AreaCode': AreaCode,
		'Currency': Currency,
		'BeginDate': BeginDate,
		'EndDate': EndDate,
		'ExpireDate': ExpireDate,
		'Status': Status,
		'NetValue': NetValue,
		'IsNewFlag': IsNewFlag,
		'Term': Term,
		'Style': Style,
		'InitMoney': InitMoney,
		'IncresingMoney': IncresingMoney,
		'Risk': Risk,
		'FinDate': FinDate,
		'SaleChannel': SaleChannel,
		'SaleChannelName': SaleChannelName,
		'IsCanBuy': IsCanBuy
	})
	time.sleep(1)

# 将数据转换为数据框
CMB_Finance = pd.concat([pd.DataFrame(data) for data in Finacing])
CMB_Finance.to_excel('/home/wangzhefeng/CMB_Finance.xlsx', index = False)








