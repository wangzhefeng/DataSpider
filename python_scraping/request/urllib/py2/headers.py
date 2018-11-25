#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-23 17:22:50
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup


# Headers
# 有些网站不会同意程序直接用上面的方式进行访问，
# 如果识别有问题，那么站点根本不会响应，所以为了完全模拟浏览器的工作，
# 我们需要设置一些Headers 的属性

# Url
# User-Agent        : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
# Content-Type      : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。在使用服务器提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务
# application/xml   ： 在 XML RPC，如 RESTful/SOAP 调用时使用
# application/json  ： 在 JSON RPC 调用时使用
# application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用


# Url
url = 'https://www.zhihu.com/'
values = {'username': '13120570880', 'password': 'wangzf711235813'}
# data = urllib.urlencode(values)

# User-Agent
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/61.0.3163.79 Chrome/61.0.3163.79 Safari/537.36'

# Referer
referer = 'https://www.zhihu.com/search?type=content&q=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90'

# Headers
headers = {'User-Agent': user_agent,
		   'Referer': referer}

request = urllib2.Request(url, data, headers)

response = urllib2.urlopen(request)

page = response.read()
