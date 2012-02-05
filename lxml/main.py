#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
main.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-11-19
'''

from lxml import etree
from urllib2 import urlopen

parser = etree.HTML(urlopen('http://google.com').read())
print type(parser)

def iterA(ele):
    for i in ele.iter('a'):
        print i,i.get('href')
iterA(parser)
