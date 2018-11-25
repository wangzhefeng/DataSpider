#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开XML文档
DOMTree = xml.dom.minidom.parse("/home/wangzhefeng/project/python/scraping/xml/xml/test.xml")
collection = DOMTree.documentElement
result = collection.getElementsByTagName("ns1:callServiceResponse")
response = result.getElementsByTagName('response')[0]
final = response.childNodes[0].data
print(final)

