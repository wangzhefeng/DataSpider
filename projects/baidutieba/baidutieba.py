#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wangzhefeng'


import urllib
import urllib2
import re

#处理页面标签类
class Tool:
    #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        #strip()将前后多余内容删除
        return x.strip()

# 百度贴吧爬虫类
class BDTB:
	# 初始化，传入基地址，是否只看楼主的参数
	def __init__(self, baseUrl, seeLZ, floorTag):
		# base链接地址
		self.baseURL = baseUrl
		# 是否只看楼主
		self.seeLZ = '?see_lz=' + str(seeLZ)
		# HTML标签剔除工具类对象
		self.tool = Tool()
		# 全局file变量，文件写入操作对象
		self.file = None
		# 楼层标号，初始为1
		self.floor = 1
		# 默认的标题，如果没有成功获取到标题的话就会用这个标题
		self.defaultTitle = '百度贴吧'
		# 是否写入楼分隔符的标记
		self.floorTag = floorTag
	# 传入页码，获取该页帖子的代码
	def getPage(self, pageNum):
		try:
			# 构建URL
			url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			return response.read()
		# 无法链接，报错
		except urllib2.URLError, e:
			if hasattr(e, "reason"):
				print "连接百度贴吧失败，错误原因", e.reason
				return None
	#获取帖子标题
	def getTitle(self, page):
	    pattern = re.compile('<h3 class=core_title_txt.*?>(.*?)</h3>',re.S)
	    result = re.search(pattern, page)
	    if result:
	        return result.group(1).strip()
	    else:
	        return None
	# 帖子数量(帖子一共有多少页)
	def getPageNum(self, page):
		pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
		result = re.search(pattern, page)
		if result:
			return result.group(1).strip()
		else:
			return None
	# 每层楼内容
	def getContent(self, page):
		pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
		items = re.findall(pattern, page)
		contents = []
		for item in items:
			# 将文本进行去除标签处理，同时在前后加入换行符
			content = "\n" + self.tool.replace(item) + "\n"
			contents.append(content) #.encode('utf-8')
		return contents

	def setFileTitle(self, title):
		# 如果标题不是None, 即成功获取到标题
		if title is not None:
			self.file = open(title + ".txt", "w+")
		else:
			self.file = open(self.defaultTitle + ".txt", "w+")

	def writeData(self, contents):
		for item in contents:
			if self.floorTag == '1':
				floorLine = "\n" + str(self.floor) + "#############################################################################\n"
				self.file.write(floorLine)
			self.file.write(item)
			self.floor += 1

	def start(self):
		indexPage = self.getPage(1)
		pageNum = self.getPageNum(indexPage)
		title = self.getTitle(indexPage)
		self.setFileTitle(title)
		if pageNum == None:
			print "URL已失效，请重试"
			return
		try:
			print "该帖子共有" + str(pageNum) + "页"
			for i in range(1, int(pageNum) + 1):
				print "正在写入第" + str(i) + "页数据"
			page = self.getPage(i)
			contents = self.getContent(page)
			self.writeData(contents)
		# 出现写入异常
		except IOError, e:
			print "写入异常，原因" + e.message
		finally:
			print "写入任务完成"

print "请输入帖子代号"
baseURL = 'http://tieba.baidu.com/p/' + str(raw_input('http://tieba.baidu.com/p/'))
seeLZ = raw_input("是否只获取楼主发言，是输入1，否输入0\n")
floorTag = raw_input("是否写入楼层信息，是输入1， 否输入0\n")
bdtb = BDTB(baseUrl = baseURL, seeLZ = seeLZ, floorTag = floorTag)
bdtb.start()
