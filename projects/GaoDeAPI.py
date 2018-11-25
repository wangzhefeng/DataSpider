#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wangzhefeng'


import requests
import re
import json
import pandas as pd

def get_site(city):
	payload = {
            'key':'a24fd793d0c22bdcc59d487482513eba',
            'keywords':'',
            'subdistrict': '0',
            'showbiz':False,
            'output':'json',
	}
	payload['keywords'] = city
	jsonData = requests.get('http://restapi.amap.com/v3/config/district?', params = payload)
	jsonText = json.loads(jsonData.text)
	# data = pd.DataFrame(
	# 	City = jsonText['districts'][0]['name'],
	# 	latitude = list(jsonText['districts'][0]['center'])[0],
	# 	longitude = jsonText['districts'][0]['center'][1],
	# 	CityCode = jsonText['districts'][0]['citycode'],
	# 	AdCode = jsonText['districts'][0]['adcode'],
	# 	Level = jsonText['districts'][0]['level']
	# )
	# center = re.search(r'\"([\d]*\.[\d]*)\,([\d]*\.[\d]*)\"', jsonText)
	# cityCode = re.search(r'\"citycode\"\:\"(\d*)\"', jsonText)
	# latitude = float(center.group(1))
	# longitude =  float(center.group(2))
	return list(jsonText['districts'][0]['center'])[0]


def main():
	data = get_site('上海')
	print(data)


if __name__ == "__main__":
	main()