#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket
import urllib.request
from urllib.error import HTTPError, URLError
import urllib.parse
import urllib.robotparser


# get request
response_get = urllib.request.urlopen("http://www.baidu.com")
print(response_get.read().decode('utf-8'))

# post request
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding = 'utf-8')
response_post = urllib.request.urlopen("http://httpbin.org/post", data = data)
print(response_post.read())


# timeout
response_get = urllib.request.urlopen("http://httpbin.org/get", timeout = 1)
print(response_get.read())


try:
	response_get = urllib.request.urlopen("http://httpbin.org/get", timeout = 0.1)
except URLError as e:
	if isinstance(e.reason, socket.timeout):
		print('TIME OUT')


## Response 
response = urllib.request.urlopen("https://www.python.org")
print(response)
print(response.status)                  # 状态码
print(response.getheaders())            # 响应头
print(response.getheader("Server"))


# Request
request = urllib.request.Request("http://www.python.org")
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))


url = "http://httpbin.org/post"
headers = {
	'User-Agent':'Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)',
	'Host':'httpbin.org'
}
dict = {
	'name':'Germey'
}
data = bytes(urllib.parse.urlencode(dict), encoding = 'utf-8')
request = urllib.request.Request(url = url, data = data, headers = headers, method = 'POST')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))


# urllib.parse
# urlparse()
result = urllib.parse.urlparse("http://www.baidu.com/index.html;user?id=5#comment")
print(type(result))
print(result)

result = urllib.parse.urlparse("www.baidu.com/index.html;user?id=5#comment", scheme = "https")
print(result)

result = urllib.parse.urlparse("http://www.baidu.com/index.html;user?id=5#comment", scheme = "https")
print(result)

result = urllib.parse.urlparse("http://www.baidu.com/index.html;user?id=5#comment", allow_fragments = False)
print(result)

result = urllib.parse.urlparse("http://www.baidu.com/index.html#comment", allow_fragments = False)
print(result)


# unurlparse()
data = ["http", "www.baidu.com", "index.html", "user", "a=6", "comment"]
print(urllib.parse.unurlparse(data))


# urljoin()
print(urllib.parse.urljoin(""))
print(urllib.parse.urljoin(""))
print(urllib.parse.urljoin(""))
print(urllib.parse.urljoin(""))
print(urllib.parse.urljoin(""))
print(urllib.parse.urljoin(""))
print(urllib.parse.urljoin(""))



# urlencode()
params= {
	'name':'germey',
	'age': 22
}
base_url = "http://www.baidu.com?"
url = base_url + urllib.parse.urlencode(params)
print(url)