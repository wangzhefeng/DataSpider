#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-23 18:56:03
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import urllib2

request = urllib2.Request(uri, data = data)
request.get_method = lambda: 'PUT' # or 'DELETE'
response = urllib2.urlopen(request)


