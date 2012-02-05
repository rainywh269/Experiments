#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib2 import urlopen

print dir(urlopen)

print type(urlopen('http://25.media.tumblr.com/tumblr_ltpde993MM1r40rvgo1_500.jpg').read())

