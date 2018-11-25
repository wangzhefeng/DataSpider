#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import json
from requests.packages import urllib3
from requests.auth import HTTPBasicAuth

from requests.exceptions import ReadTimeout 
from requests.exceptions import ConnectTimeout
from requests.exceptions import HTTPError
from requests.exceptions import RequestException
from requests.exceptions import ConnectionError



# A Example
response = requests.get("http://www.baidu.com/")

print(response)
print(type(response))
print(response.status_code)
print(response.text)
print(response.cookies)
print(response.headers)
print(response.history)
#=========================================================================
#                                  get
#=========================================================================
response = requests.get("http://httpbin.org/get")
print(response.text)
#=====================================================================
# get request with parameter method 1
response = requests.get("http://httpbin.org/get?name=germey&age=22")
print(response.text)

# get request with parameter method 2
data = {
	'name':'germey',
	'age':22
}
response = requests.get("http://httpbin.org/get", params = data)
print(response.text)
#=====================================================================
#解析json
response = requests.get("http://httpbin.org/get")
print(type(response.text))

print(response.json())
print(json.loads(response.text))

print(type(response.json()))
print("---------------------------------\n")
#=====================================================================
# 获取二进制数据(img)
response = requests.get("https://github.com/favicon.ico")
print(type(response.text))
print(type(response.content))
print(response.text)
print(response.content)

with open("favicon.ico", "wb") as f:
	f.write(response.content)
	f.close()
#=====================================================================
 # 添加headers
response = requests.get("https://www.zhihu.com/explore")
print(response.text)
print("---------------------------------\n")
headers = {
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/61.0.3163.79 Chrome/61.0.3163.79 Safari/537.36'
}
response = requests.get("https://www.zhihu.com/explore", headers = headers)
print(response.text)
#===================================================================================
#                                     post
#===================================================================================
data = {
	'name':'germey',
	'age':'22'
}
headers = {
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/61.0.3163.79 Chrome/61.0.3163.79 Safari/537.36'
}
response = requests.post("http://httpbin.org/post", data = data)
print(response.text)

response = requests.post("http://httpbin.org/post", data = data, headers = headers)
print(response.json())
#====================================================================================
#                                 response属性
#====================================================================================
response = requests.get("http://jianshu.com")
print(type(response.status_code), response.status_code)
print(type(response.headers), response.headers)
print(type(response.cookies), response.cookies)
print(type(response.url), response.url)
print(type(response.history), response.history)

# 状态码判断
response = requests.get("http://jianshu.com")
exit() if not response.status_code == requests.codes.ok else print('Request Successfully')
exit() if not response.status_code == 200 else print('Request Successfully')

response = requests.get("http://jianshu.com/hello.html")
exit() if not response.status_code == requests.codes.not_found else print('404 Not Found')
exit() if not response.status_code == 404 else print('404 Not Found')

#==========================================================================================
#                                    高级操作
#==========================================================================================
# 文件上传
files = {'file':open('favicon.ico', 'rb')}
response = requests.post("http://httpbin.org/post", files = files)
print(response.text)

# 获取cookie
response = requests.get("https://www.baidu.com")
print(response.cookies)
for key, value in response.cookies.items():
	print(key + '=' + value)

# 会话维持
requests.get("http://httpbin.org/cookies/set/number/123456789")
response = requests.get("http://httpbin.org/cookies")
print(response.text)

s = requests.Session() # session 对象
s.get("http://httpbin.org/cookies/set/number/123456789")
response = s.get("http://httpbin.org/cookies")
print(response.text)

# 证书验证
# response = requests.get("https://www.12306.cn")
# print(response.status_code)

# from requests.packages import urllib3
urllib3.disable_warnings()
response = requests.get("https://www.12306.cn", verify = False)
print(response.status_code)


# 设置代理
# proxies = {
# 	"http":"http://127.0.0.1:9743",
# 	"https":"https://127.0.0.1:9743"
# }

# 超时设置
response = requests.get("http://www.taobao.com", timeout = 1)
print(response.status_code)

try:
	response = requests.get("http://httpbin.org/get", timeout = 0.01)
	print(response.status_code)
except ReadTimeout:
	print('ReadTimeout error')
except ConnectTimeout:
	print('ConnectTimeout error')


print('=============================================\n')
# 认证设置

r = requests.get("http://120.27.34.24:9001")
print(r.status_code)

# from requests.auth import HTTPBasicAuth
r = requests.get("http://120.27.34.24:9001", auth = HTTPBasicAuth('user', '123'))
print(r.status_code)

r = requests.get("http://120.27.34.24:9001", auth = ('user','123'))
print(r.status_code)


# from requests.exceptions import ReadTimeout, HTTPError, RequestException, ConnectionError 
try:
	response = requests.get("http://httpbin.org/get", timeout = 0.1)
	print(response.status_code)
except ReadTimeout:
	print("ReadTimeout error")
except ConnectTimeout:
	print("ConnectTimeout Error")
except ConnectionError:
	print("Connection Error")
except HTTPError:
	print("HTTP error")
except RequestException:
	print("Error")