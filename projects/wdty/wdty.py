#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-09 21:56:05
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import requests
import re
import pandas as pd

# 设置头部信息
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11', 
		   'Accept':'text/html;q=0.9,*/*;q=0.8',
		   'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		   'Connection':'close',
		   'Referer':'https://www.bluewhale.cc/'}

# 提取Web页面内容
r = requests.get('http://www.p2peye.com/shuju/ptsj/', headers = headers)
html = r.content
html = str(html, encoding = 'GBK')

# 使用正则表达式提取字段信息
title = re.findall(r'"return false".*?title="(.*?)"', html)
total = re.findall(r'"total">(.*?)万<', html)
rate = re.findall(r'"rate">(.*?)<', html)
pnum = re.findall(r'"pnum">(.*?)人<', html)
cycle = re.findall(r'"cycle">(.*?)月<', html)
p1num = re.findall(r'"p1num">(.*?)人<', html)
fuload = re.findall(r'"fuload">(.*?)分钟<', html)
alltotal = re.findall(r'"alltotal">(.*?)万<', html)
capital = re.findall(r'"capital">(.*?)万<', html)

# 
import time
date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
print(date)

# 设置数据表的个字段顺序
columns = ['采集日期',
		   '平台名称',
		   '成交额(万)',
		   '综合利率',
		   '投资人(人)',
		   '借款周期(月)',
		   '借款人(人)',
		   '满标速度(分钟)',
		   '累计贷款余额(万)',
		   '净资金流入(万)']
table = pd.DataFrame({'采集日期':date,
		   			  '平台名称':title,
		   			  '成交额(万)':total,
		   			  '综合利率':rate,
		   			  '投资人(人)':pnum,
		   			  '借款周期(月)':cycle,
		   			  '借款人(人)':p1num,
		   			  '满标速度(分钟)':fuload,
		   			  '累计贷款余额(万)':alltotal,
		   			  '净资金流入(万)':capital}, 
		   			  columns = columns)
# 数据导出
table.to_csv('E:\\GitHub\\python\\scraping\\WDTY_data\\wdty.csv', index = False, mode = 'a')


#################################################################################################
def loan_data():
	import os
	import requests
	import re
	import pandas as pd
	import time
	
	start = time.clock()
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11', 
			   'Accept':'text/html;q=0.9,*/*;q=0.8',
		   	   'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		       'Connection':'close',
		       'Referer':'https://www.bluewhale.cc/'}
	url = 'http://www.p2peye.com/shuju/ptsj/'
	r = requests.get(url, headers = headers)
	status = r.status_code
	if status == 200:
		print('页面抓取状态正常。')
	else:
		os._exit(0)
	html = r.content
	html = str(html, encoding = "GBK")
	print('编码转换完成！')
	
	title = re.findall(r'"return false".*?title="(.*?)"', html)
	total = re.findall(r'"total">(.*?)万<', html)
	rate = re.findall(r'"rate">(.*?)<', html)
	pnum = re.findall(r'"pnum">(.*?)人<', html)
	cycle = re.findall(r'"cycle">(.*?)月<', html)
	p1num = re.findall(r'"p1num">(.*?)人<', html)
	fuload = re.findall(r'"fuload">(.*?)分钟<', html)
	alltotal = re.findall(r'"alltotal">(.*?)万<', html)
	capital = re.findall(r'"capital">(.*?)万<', html)
	date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
	print('数据提取完成！')

	columns = ['采集日期',
			   '平台名称',
			   '成交额(万)',
			   '综合利率',
			   '投资人(人)',
			   '借款周期(月)',
			   '借款人(人)',
			   '满标速度(分钟)',
			   '累计贷款余额(万)',
			   '净资金流入(万)']
	table = pd.DataFrame({'采集日期': date,
						  '平台名称': title,
						  '成交额(万)': total,
						  '综合利率': rate, 
						  '投资人(人)': pnum,
						  '借款周期(月)': cycle,
						  '借款人(人)': p1num,
						  '满标速度(分钟)': fuload,
						  '累计贷款余额(万)': alltotal,
						  '净资金流入(万)': capital},
						  columns = columns)
	print('数据表创建完成！')

	table.to_csv('C:\\Users\\cliffwang\\Desktop\\wdty'+date+'.csv',index=False)
	print(date+'日数据导出完毕！')
	
	table.to_csv('wdty.csv',index=False,mode='a')
	print('累计数据追加导出完毕！')
	
	end = time.clock()
	print ("执行时间: %f s" % (end-start))


