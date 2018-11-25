#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

urls = []
for year in range(2011, 2018):
	for month in range(1, 13):
		if year <= 2016:
			urls.append('http://tianqi.2345.com/t/wea_history/js/58362_%s%s.js' % (year, month))
		else:
			if month < 10:
				urls.append('http://tianqi.2345.com/t/wea_history/js/%s0%s/58362_%s0%s.js' % (year, month, year, month))
			else:
				urls.append('http://tianqi.2345.com/t/wea_history/js/%s%s/58362_%s%s.js' % (year, month, year, month))
print(urls)
print(len(urls))


url = urls[0]
response = requests.get(url = url).text
print(response)


# 正则匹配
ymd = re.findall("ymd:'(.*?)',",response)
high = re.findall("bWendu:'(.*?)℃',",response)
low = re.findall("yWendu:'(.*?)℃',",response)
tianqi = re.findall("tianqi:'(.*?)',",response)
fengxiang = re.findall("fengxiang:'(.*?)',",response)
fengli = re.findall(",fengli:'(.*?)'",response)
aqi = re.findall("aqi:'(.*?)',",response)
aqiInfo = re.findall("aqiInfo:'(.*?)',",response)
aqiLevel = re.findall(",aqiLevel:'(.*?)'",response)