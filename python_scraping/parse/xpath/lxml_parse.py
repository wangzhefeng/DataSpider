#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "wangzhefeng"

# XPath
	# nodename
	# /
	# //
	# .
	# ..
	# @


from lxml import etree


# ---------------------------------------------------------
# parse html string
# ---------------------------------------------------------
text1 = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''

html1 = etree.HTML(text1)
res1 = etree.tostring(html1)
print(res1.decode("utf-8"))


# ---------------------------------------------------------
# parse html file
# ---------------------------------------------------------
html2 = etree.parse("./test_lxml.html", etree.HTMLParser())
res2 = etree.tostring(html2)
print(res2.decode("utf-8"))

# ---------------------------------------------------------
# 所有节点
# ---------------------------------------------------------
res_all_nodes = html1.xpath("//*")
print(res_all_nodes)

res_all_li = html1.xpath("//li")
print(res_all_li)

