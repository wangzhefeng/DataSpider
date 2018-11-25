#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyquery import PyQuery as pq

##################### 初始化 ######################
# 字符创初始化
html = '''
	<div class="wrap">
		<div id="container">
			<ul class="list">
				<li class="item-0">first item</li>
				<li class="item-1"><a href="link2.html">second item</a></li>
				<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
				<li class="item-1 active"><a href="link4.html">fourth item</a></li>
				<li class="item-0"><a href="link5.html">fifth item</a></li>
			</ul>
		</div>
	</div>
'''
doc = pq(html)
print(doc('li'))
print('-------------------------------------------\n')

# URL初始化
doc = pq(url = "http://www.baidu.com")
print(doc('head'))
print('-------------------------------------------\n')

# 文件初始化
doc = pq(filename = 'demo.html')
print(doc('script'))
print('-------------------------------------------\n')

################# 基本CSS选择器######################
doc = pq(html)
print(doc('#container .list li'))

#################### 查找元素 ##########################
# 子元素
doc = pq(html)
items = doc('.list')    # css selector
# print(type(items))
# print(items)

lis = items.find('li')  # find()
print(type(lis))
print(lis)

lis = items.children()  # children()
print(type(lis))
print(lis)

lis = items.children('.active') # CSS selector
print(lis)
#---------------------------------------
# 父元素(祖先节点)
doc = pq(html)
items = doc('.list')
container = items.parent() # parent()
print(container)

doc = pq(html)
items = doc('.list')
parents = items.parents()  #parents()
print(parents)

parent = items.parents('.wrap')
print(parent)
#---------------------------------------
# 兄弟元素
doc = pq(html)
li = doc('.list .item-0.active')
print(li.siblings())       # siblings()

print(li.siblings('.active'))

#--------------------------------------
# 遍历
doc = pq(html)
li = doc('.item-0.active')
print(li)

lis = doc('li').items()
print(type(lis))

for li in lis:
	print(li)


################### 获取信息 #################################
# 获取属性
doc = pq(html)
a = doc('.item-0.active a')
print(a)
print(a.attr('href'))
print(a.attr.href)

# 获取文本
doc = pq(html)
a = doc('.item-0.active a')
print(a)
print(a.text())

# 获取HTML
doc = pq(html)
li = doc('.item-0.active')
print(li)
print(li.html())

################### DOM 操作 ################################
# addClass
# removeClass

doc = pq(html)
li = doc('.item-0.active')
print(li)
li.removeClass('active')
print(li)
li.addClass('active')
print(li)

# attr
# css
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.attr('name', 'link')
print(li)
li.css('font-size', '14px')
print(li)

# remove()
html = '''
	<div class='wrap'>
		Hello,World
		<p>This is a paragraph</p>
	</div>
	'''
doc = pq(html)
wrap = doc('.wrap')
print(wrap.text())
wrap.find('p').remove()
print(wrap.text())

# 伪类选择器
html = '''
	<div class="wrap">
		<div id="container">
			<ul class="list">
				<li class="item-0">first item</li>
				<li class="item-1"><a href="link2.html">second item</a></li>
				<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
				<li class="item-1 active"><a href="link4.html">fourth item</a></li>
				<li class="item-0"><a href="link5.html">fifth item</a></li>
			</ul>
		</div>
	</div>
'''
doc = pq(html)
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:gt(2)')
print(li)
li = doc('li:nth-child(2n)')
print(li)
li = doc('li:contains(second)')
print(li)