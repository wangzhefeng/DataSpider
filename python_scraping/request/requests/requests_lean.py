#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

########################################################################
#                                 快速上手
########################################################################
# 1. 发送请求
r_get = requests.get("http://github.com/timeline.json")
print(r_get.text)
r_post = requests.post("http://httpbin.org/post")
r_put = requests.put("http://httpbin.org/put")
r_delete = requests.delete("http://httpbin.org/delete")
r_head = requests.head("http://httpbin.org/get")
r_options = requests.options("http://httpbin.org/get")
#----------------------------------------------------------------------
# 2. 传递URL参数——为URL的查询字符串(query string)传递数据
payload1 = {'key1': 'value1', 'key2': 'value2'}
r_1 = requests.get("http://httpbin.org/get", params = payload1)
print(r.url)

payload2 = {'key': 'value', 'key2': ['value2', 'value3']}
r_2 = requests.get("http://httpbin.org/get", params = payload2)
print(r_2)

#----------------------------------------------------------------------
# 3.响应内容
r = requests.get("http://github.com/timeline.json")
print(r.text)
print(r.encoding)
print(r.content)          # 对于HTML&XML找到其编码
r.encoding = "ISO-8859-1" # 改变文本编码

#----------------------------------------------------------------------
# 4.二进制响应内容
print(r.content)
from PIL import Image
from io import BytesIO
i = Image.open(BytesIO(r.content))

#----------------------------------------------------------------------
# 5.JSON响应内容(requests内置解码器)
r = requests.get("https://github.com/timeline.json")
print(r.json())
# 如果成功调用r.json()并不意味着响应的成功，有的服务器会在失败的响应中包含一个JSON对象，这种JSON会被解码返回.
# 要检查请求是否成功，应该使用r.raise_for_status()或者r.status_code是否和你的期望相同
print(r.raise_for_status)
print(r.status_code)

#----------------------------------------------------------------------
# 6.原始响应内容
# 获取来自服务器的原始套接字响应
r = requests.get("https://github.com/timeline.json", stream = True)
print(r.raw)
print(r.raw.read(10))

# with open(filename, 'wb') as fd:
# 	for chunk in r.iter_content('chunk_size'):
# 		fd.write(chunk)

#----------------------------------------------------------------------
# 7.定制请求头
url = "http://api.github.com/some/endpoint"
headers = {
	'user-agent': 'my-app/0.0.1'
}
r = requests.get(url, headers = headers)
print(r.text)
#----------------------------------------------------------------------
# 8.更复杂的post请求
# 发送一些编码为表单的数据-非常像一个HTML表单
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data = payload)
print(r.text)

payload = (('key1', 'value1'), ('key1', 'value2'))
r = requests.post("http://httpbin.org/post", data = payload)
print(r.text)

# 编码位JSON的POST/PATCH数据
import json
url = "https://api.github.com/some/endpoint"
payload = {'some': 'data'} # dict
r = requests.post(url = url, data = json.dumps(payload))

# 使用json参数直接传递，会被自动编码
url = "https://api.github.com/some/endpoint"
payload = {'some': 'data'}
r = requests.post(url = url, json = payload)

#----------------------------------------------------------------------
# 9.POST一个多部分编码(Multipart-Encoded)的文件
url = "http://httpbin.org/post"
files = {'file': open('/home/wangzhefeng/project/python/scraping/report.xls', 'rb')}
print(r.text)
# 显式设置文件名,文件类型,请求头
url = "http://httpbin.org/post"
files = {'file': ('/home/wangzhefeng/project/python/scraping/report.xls',
                  open('report.xls', 'rb'),
                  'application/vnd.ms-excel',
                  {'Expire': '0'})}
r = requests.post(url, files = files)
print(r.text)


#----------------------------------------------------------------------
# 10.响应状态码
r = requests.get("http://httpbin.org/get")
print(r.status_code)
# requests内置状态码查询对象
print(r.status_code == requests.codes.ok)

# 如果发送了一个错误请求(4XX:客户端错误，5XX服务器错误),抛出异常
bad_r = requests.get("http://httpbin.org/status/404")
print(bad_r.status_code)
bad_r.raise_for_status()



#-----------------------------------------------------------------------
# 11.响应头
# headers是一个以python字典形式展示的,HTTP头部是大小写不敏感的
r = requests.get('http://www.baidu.com')
print(r.headers)
print(r.headers['Content-Type'])
print(r.headers.get('content-type'))

#----------------------------------------------------------------------
# 12.Cookie
url = "http://example.com/some/cookie/setting/url"
r = requests.get(url = url)
# 访问cookie
print(r.cookies['example_cookie_name'])

# 发送cookie
url = "http://httpbin.org/cookies"
cookies = dict(cookies_are = "working")
r = requests.get(url = url, cookies = cookies)
print(r.text)

# Cookie的返回对象是RequestsCookiejar,他的行为和字典类似，但界面更为完整，适合跨域名跨路径使用，可以把Cookie Jar传到Requests中
jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain = 'httpbin.org', path = '/cookies')
jar.set('gross_cookie', 'blech', domain = 'httpbin.org', path = '/elsewhere')
r = requests.get(url, cookies = jar)
print(r.text)

#----------------------------------------------------------------------
# 13.重定向与请求历史
# 默认情况下,除了HEAD,Requests会自动处理所有重定向,可以使用响应对象的history方法来跟踪重定向
# Response.history是一个Response对象的列表, 为了完成请求而创建了这些对象。
# 这些列表按照从最老到最新的请求进行排序.
r = requests.get("http://github.com")
print(r.url)
print(r.status_code)
print(r.history)
# 如果使用的是GET,POST,OPTIONS,PUT,PATCH, DELETE,可以使用allow_redirect参数禁用重定向处理
r = requests.get("http://github.com", allow_redirects = False)
print(r.status_code)
print(r.history)
# 如果使用了HEAD,可以启用重定向
r = requests.head("http://github.com", allow_redirects = False)
print(r.url)
print(r.history)

#----------------------------------------------------------------------
# 14.超时
r = requests.get("http://github.com", timeout = 0.001)
print(r)

#----------------------------------------------------------------------
# 15.错误与异常
# class requests.exceptions.RequestException

# 网络错误(DNS查询失败,拒绝连接):                            ConnectionErrror
# HTTP请求返回不成功的状态码: Response.raise_for_status()--> HTTPError
# 请求超时:                                                  Timeout
# 请求超过了设定的最大重定向次数:                            TooManyRedirects


#=======================================================
#                   身份认证
#=======================================================
# 基本身份认证
# 以HTTP Basic Auth发送请求
from requests.auth import HTTPBasicAuth
requests.get('https://api.github.com/usr', auth = HTTPBasicAuth('user', 'pass'))
requests.get('https://api.github.com/user', auth = ('user', 'pass'))
# netrc认证
# 如果认证方法没有收到auth参数，Requests将试图从用户的netrc文件中获取URL的hostname需要的认证身份
# 如果找到了 hostname 对应的身份，就会以 HTTP Basic Auth 的形式发送请求

#------------------------------------------
# 摘要身份认证
from requests.auth import HTTPDigestAuth
url = "http://httpbin.org/digest-auth/auth/user/pass"
requests.get(url = url, auth = HTTPDigestAuth('user', 'pass'))

# OAuth 1 认证
import requests
from requests_oauthlib import OAuth1

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KAY', 'YOUR_APP_SERECT',
              'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
requests.get(url = url, auth = auth)

#----------------------------------------
# OAuth 2 与 OpenID连接认证

#---------------------------------------
# 其他身份认证形式

#---------------------------------------
# 新的身份认证形式