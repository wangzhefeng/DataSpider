#!/usr/bin/env python
# -*- coding: utf-8 -*-

# DOM parse

def dom_parser(gz):
	import gzip, cStringIO
	import xml.dom.minidom

	cs_cnt = 0
	str_s = ''
	file_io = cStringIO.StringIO()
	xm = gzip.open(gz, 'rb')
	print("已读入：%s.\n解析中：" % (os.path.abspath(gz)))

	doc = xml.dom.minidom.parseString(xm.read())
	bulkPmMrDataFile = doc.documentElement

	# 读入子元素
	enbs = bulkPmMrDataFile.getElementsByTagName('eNB')
	measurements = enbs[0].getElementsByTagName('measurement')
	objects = measurements[0].getElementsByTagName('object')

