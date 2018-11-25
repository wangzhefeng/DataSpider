#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wangzhefeng'

'''
总的来说 sax解析xml进行3个阶段, sax是线性解析, 对于大的xml会很有效率
'''

import xml.sax
# from xml.sax import parse
import xml.sax.handler
# from xml.sax.handler import ContentHandler
import pprint

import xml.dom.minidom

DOMTree = xml.dom.minidom.parse('''''')
