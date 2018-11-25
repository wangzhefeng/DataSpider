#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''获取经纬度'''

import json
import requests
import csv
import pandas as pd
import traceback
import os


# data
os.chdir('/home/wangzhefeng/Downloads/baidu_hotmap')
data = pd.read_csv('sh_house.csv')
print(data)


def get_lng_lat(add):
	output = 'json'
	ak = 'j7cG5j1Vm3yGfexFZ62cqpoM0Cq9kpg6'
	params = json.dumps({
		'address': add,
		'output': output,
		'ak': ak
	})
	url = 'http://api.map.baidu.com/geocoder/v2/'
	request = requests.get(url = url, params = params)
	print(request.url)
	lng_lat = request.text
	js = json.loads(lng_lat)
	print(js)
	return js


file = open('经纬度.json', 'w')
with open('sh_house.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for line in reader:
		if reader.line_num == 1:
			continue
		b = line[0].strip()
		c = str(line[1].strip())
		try:
			lng = get_lng_lat(b)['result']['location']['lng']
			lat = get_lng_lat(b)['result']['location']['lat']
			str_temp = '{"lat":' + str(lat) + ',{"lng":' + str(lng) + ',"count":' + str(c) + '},'
			file.write(str_temp)
		except:
			f = open('异常日志.txt', 'a')
			traceback.print_exc(file = f)
			f.flush()
			f.close()
			print('发生异常')
file.close()




def main():
	add = data['xiaoqu']
	for i in add:
		print(i)
	# 	get_lng_lat(i)

if __name__ == '__main__':
	main()
