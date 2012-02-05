#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
testCrawler.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-11-25
'''

import urllib2
import httplib
if __name__ == '__main__':
    conn = httplib.HTTPConnection("www.cnbeta.com")
    conn.request("HEAD",'')
    res = conn.getresponse()
    print res.status,res.reason
    print res.read()
    print dir(res),res.getheaders()
    conn.request("GET",'')
    res = conn.getresponse()
    print res.status,res.reason
    print res.read()
