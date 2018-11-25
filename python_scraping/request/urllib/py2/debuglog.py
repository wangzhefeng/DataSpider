#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-23 18:59:01
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import urllib2

httpHandler = urllib2.HTTPHandler(debuglevel = 1)
httpsHandler = urllib2.HTTPSHandler(debuglevel = 1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')
