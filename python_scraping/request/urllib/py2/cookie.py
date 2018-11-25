#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-23 19:23:43
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

import urllib
import urllib2
import cookielib

########################################################
# 			     将cookie保存到一个对象中
########################################################
# 声明一个CookieJar对象实例来保存cookie
cooike = cookielib.CookieJar()
# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = urllib2.build_opener(handler)
# 此处的open方法同urllib2的urlopen方法也可以传入request
response = opener.open('http://www.baidu.com')

for item in cookie:
	print 'Name = ' + item.name
	print 'Value = ' + item.value


#########################################################
#						将cookie写入文件
#########################################################
# 设置保存cookie的文件，统计目录下的cookie.txt
filename = 'cookie.txt'

# 声明一个MozillaCookieJar对象实例来保存cookie,之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
# 利用urllib2库的HTTPCookieProcessor对象创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = urllib2.build_opener(handler)
# 创建一个请求，原理同urllib2的urlopen
url = 'http://www.baidu.com'
response = opener.open(url)

# 保存cookie到文件
cookie.save(ignore_discard = True, ignore_expires = True)


#########################################################
#			         从文件中获取Cookie并访问
#########################################################
# 创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
# 从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard = True, ignore_expires = True)

# 利用urllib2库的HTTPCookieProcessor对象创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)

# 利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(handler)

# 创建请求的request
url = 'http://www.baidu.com'
req = urllib2.Request(url)

response = opener.open(req)
print response.read()

########################################################
#					利用cookie模拟网站登录
########################################################
filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)

handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)

postdata = urllib.urlencode({
            'stuid':'201200131012',
            'pwd':'23342321'
        })
#登录教务系统的URL
loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
#模拟登录，并把cookie保存到变量
result = opener.open(loginUrl, postdata)
#保存cookie到cookie.txt中
cookie.save(ignore_discard = True, ignore_expires = True)
#利用cookie请求访问另一个网址，此网址是成绩查询网址
gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
#请求访问成绩查询网址
result = opener.open(gradeUrl)
print result.read()