#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# py2 & py3
from bs4 import BeautifulSoup
import urllib.request
import lxml

#################################################################
#                          1. Hello World
#################################################################
# BeautifulSoup()

# 解析器
# BeautifulSoup(markup, "html.parser")
# BeautifulSoup(markup, "lxml")
# BeautifulSoup(markup, "xml")
# BeautifulSoup(markup, "html5lib")
#################################################################
html_doc = """
		   <html><head><title>The Dormouse's story</title></head>
		   <body>
		   <p class="title"><b>The Dormouse's story</b></p>

		   <p class="story">Once upon a time there were three little sisters; and their names were
		   <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
		   <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
		   <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
		   and they lived at the bottom of a well.</p>

		   <p class="story">...</p>
		   """
# html_doc = urllib.request.urlopen(html_doc)
soup = BeautifulSoup(html_doc, "lxml")
print(soup.prettify())


# get the tag and tag's name, text, parent_tag and attribute
# .tag
print(soup.title)

# .tag.name
print(soup.title.name)

# .tag.string  # .tag.get_text()
print(soup.title.string)
print(soup.title.get_text())

# .tag.parent.name
print(soup.title.parent.name)

# .tag['class'] # .tag.get('class') # .tag.attrs['']
print(soup.p['class'])
print(soup.p.attrs['class'])
print(soup.p.get('class'))

# findAll() | find_all() & find()
print(soup.a)
print(soup.findAll('a'))
print(soup.find_all('a'))
print(soup.find(id = "link3"))

#################################################################
#                     BeautifulSoup object
#################################################################
# soup = BeautifulSoup(open(b'E:\\GitHub\\python\\scraping\\index.html'))
# print(soup)

soup = BeautifulSoup('<html>data</html>', 'lxml')
print(soup)

soup = BeautifulSoup('Sacr&eacute; bleu!', 'lxml')
print(soup)
#################################################################
#                          对象的种类
#################################################################

# Tag------------------ 
soup = BeautifulSoup('<b class = "boldest">Extremely blod</b>', 'lxml')
print(soup)

# tag
tag = soup.b
print(type(tag))

# tag-name
print(tag.name)
tag.name = 'blockquote'
print(tag)

# tag-attribute
print(tag['class'])
print(tag.get('class'))
print(tag.attrs)

# example
tag['class'] = 'verybold'
tag['id'] = 1
print(tag)

del tag['class']
del tag['id']
print(tag)
print(tag.get('class'))
print(tag.get('id'))


# 多值属性

# NavigableString(可以遍历的字符串)-----------------------




# BeautifulSoup----------------------------------------
print(soup.name)


# Comment(注释及特殊字符串)-------------------------------
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, 'lxml')
comment = soup.b.string
print(comment)
print(type(comment))


#################################################################
#                          遍历文档树
#################################################################
html_doc = """
		   <html><head><title>The Dormouse's story</title></head>
		   <body>
		   <p class="title"><b>The Dormouse's story</b></p>

		   <p class="story">Once upon a time there were three little sisters; and their names were
		   <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
		   <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
		   <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
		   and they lived at the bottom of a well.</p>

		   <p class="story">...</p>
		   """
soup = BeautifulSoup(html_doc, 'lxml')

############# 子节点（子孙节点） ###############
## tag.name
print(soup.head)
print(soup.title)
print(soup.body.b)
print(soup.a)
print(soup.find_all())

## .contents & .children
head_tag = soup.head
print(head_tag)
print(head_tag.contents)
print(type(head_tag.contents))   # list
title_tag = head_tag.contents[0]
print(title_tag)
print(title_tag.contents)
print(soup.contents)
print(len(soup.contents))
print(soup.contents[0].name)
#----------------------------
print(title_tag.children)        # iter
print(type(title_tag.children))
for child in title_tag.children:
	print(child)

## .descendants
print(haed_tag.descendants)
print(type(head_tag.descendants)) # iter
for child in head_tag.descendants:
	print(child)
print(len(list(soup.children)))
print(len(list(soup.descendants)))

# string
print(title_tag.string)

# strings
for string in soup.strings:
	print(string)

# stripped_strings
for string in soup.stripped_strings:
	print(string)
#################### 父节点（祖先节点） #############
## .parent
print(title_tag.parent)
print(title_tag.string.parent)
html_tag = soup.html
print(html_tag.parent)

## .parents 
link = soup.a
link
for parent in link.parents:
	if parent is None:
		print(parent)
	else:
		print(parent.name)
##################### 兄弟节点 ####################
# .next_sibling
# .previous_sibling

# .next.siblings
# .previous_siblings
#################### 回退和前进 ###################
# .next_element
# .previous_element

# .next_elements
# .previous_element
#################################################################
#                          搜索文档树
#################################################################
# find_all()
print(soup.find_all('tag'))
print(soup.find_all('tag')[0])
print(soup.find_all('tag')[0:2])
print(soup.find_all(attrs = {'key':'value'}))
print(soup.find_all(id = 'attr_name'))
print(soup.find_all(class_ = 'attr_name'))
print(soup.find_all(text = 'text'))
# find()
print(soup.find('tag'))
print(soup.find_all('tag')[0])
print(soup.find(attrs = {'key':'value'}))
print(soup.find(id = 'attr_name'))
print(soup.find(class_ = 'attr_name'))
print(soup.find(text = 'text'))
# find_parent() find_parents()
# find_next_sibling() find_previous_sibling
# find_next_siblings() find_previous_siblings
# find_all_next() find_next()
# find_all_previous() find_previous()

########################## CSS selector
# select()
# select tag
print(soup.select('.class .class'))
print(soup.select('#id .class'))
print(soup.select('tag tag'))
print(soup.select('tag')[0])
for tag in soup.select('tag'):
	print(tag.select('tag'))
# select attribute
print(soup.select('tag')['attr'])
print(soup.select('tag').attrs['attr'])
# select text
print(soup.select('tag').get_text())
#################################################################
#                          修改文档树
#################################################################



#################################################################
#                            输出
#################################################################

