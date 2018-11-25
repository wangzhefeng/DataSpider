#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-23 18:09:03
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import urllib
import urllib2

# Proxy 代理设置
# urllib2 默认会使用环境变量 
# http_proxy 
# 来设置 
# HTTP Proxy。
# 假如一个网站它会检测某一段时间某个
# IP 
# 的访问次数，如果访问次数过多，它会禁止你的访问。
# 所以你可以设置一些代理服务器来帮助你做工作，每隔一段时间换一个代理，网站君都不知道是谁在捣鬼了

enable_proxy = True

proxy_handler = urllib2.ProxyHander({"http": 'http://some-proxy.com:8000'})
null_proxy_handler = urllib2.ProxyHander({})

if enable_proxy:
	opener = urllib2.build_opener(proxy_handler)
else:
	opener = urllib2.build_opener(null_proxy_handler)

urllib2.install_opener(opener)

