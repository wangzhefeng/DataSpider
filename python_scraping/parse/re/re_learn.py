#!/usr/bin/env python
# -*- coding: utf-8 -*-



"""
返回pattern对象
# pattern = re.compile(string[, flag])

# 七种匹配函数
# re.match(pattern, string[, flags])
	- 从字符串的起始位置匹配正则表达式
# re.search(pattern, string[, flags])
	- 扫描整个字符串，返回第一个成功匹配正则表达式的结果
# re.split(pattern, string[, maxsplit])
# re.findall(pattern, string[, flags])
	- 搜索整个字符串，返回匹配正则表达式的所有内容
# re.finditer(pattern, string[, flags])
# re.sub(pattern, repl, string[, count])
	- 搜索整个字符串，将匹配正则表达式的字符串进行替换
# re.subn(pattern, repl, string[, count])

方法
# .group()
# .group(1, 2, 3)
# .groups()
# .groupdict()
# .start(2)
# .end(2)
# .span(1)
# .expand(r'\2 \1\3')

属性
# .string
# .re
# .pos
# .endpos
# .lastindex
# .lastgroup


正则表达式语法知识：
	()  : 匹配目标
	.*  : 万能匹配(贪婪模式)
	.*? : 万能匹配(非贪婪模式)
	修饰符: re.I
		    re.L
		    re.S
		    re.M
		    re.U
		    re.X
	转义字符: \(
			  \)
			  \.
			  \\
			  ...
"""


import re


# ----------------------------------------------------------
# 使用 re.match() 匹配文本，获得匹配结果，无法匹配返回None
pattern = re.compile('hello')

result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'helloo wangzf')
result3 = re.match(pattern, 'helo wangzf')
result4 = re.match(pattern, 'hello wangzf')
if result1:
	print(result1.group())
else:
	print('1 匹配失败')

if result2:
	print(result2.group())
else:
	print('2 匹配失败')

if result3:
	print(result3.group())
else:
	print('3 匹配失败')

if result4:
	print(result4.group())
else:
	print('4 匹配失败')


pattern  = re.compile(r'(\w+) (\w+)(?P<sign>.*)')
m = re.match(pattern, 'hello world!')
print(m.string)     		# 'hello world!'
print(m.re)					# re.compile('(\\w+) (\\w+)(?P<sign>.*)')
print(m.pos)				# 0
print(m.endpos)				# 12
print(m.lastindex)			# 3
print(m.lastgroup)			# sign
print(m.group())			# hello world!
print(m.group(1, 2, 3)) 	# ('hello', 'world', '!')
print(m.groups())			# ('hello', 'world', '!')
print(m.groupdict())		# {'sign': '!'}
print(m.start(2))			# 6
print(m.end(2))				# 11
print(m.span(1))			# (0, 5)
print(m.expand(r'\2 \1\3')) # world hello!

###################################################
# re.search()
pattern = re.compile(r'world')
m = re.search(pattern, 'hello world!')
if m:
	print(m.group())
else:
	print('搜索失败')

print(m.string)
print(m.re)
print(m.pos)
print(m.endpos)
print(m.lastindex)
print(m.lastgroup)
print(m.group())
# print(m.group(1, 2, 3))
print(m.groups())
print(m.groupdict())
print(m.start())
print(m.end())
print(m.span())
# print(m.expand(r'\2 \1\3'))
###################################################
# re.split()
pattern = re.compile(r'\d+')
m = re.split(pattern, 'one1two2three3four')
print(m)
##################################################
# re.findall()
pattern = re.compile(r'\d+')
m = re.findall(pattern, 'one1two2three3four4')
print(m)
#################################################
# re.finditer()
pattern = re.compile(r'\d+')
m = re.finditer(pattern, 'one1two2three3four4')
for i in m:
	print(i.group())
#################################################
# re.sub()
pattern = re.compile(r'(\w+) (\w+)')
s = 'i say,hello world'

m = re.sub(pattern, r'\2 \1', s)
print(m)

def func(x):
	return x.group(1).title() + ' ' + x.group(2).title()
m = re.sub(pattern, func, s)
print(m)
##################################################
# re.subn()
pattern = re.compile(r'(\w+) (\w+)')
s = 'i say,hello world,my god'

m = re.subn(pattern, r'\2 \1', s)
print(m)

def func(x):
	return x.group(1).title() + ' ' + x.group(2).title()
m = re.subn(pattern, func, s)
print(m)