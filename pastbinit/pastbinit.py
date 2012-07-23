#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
from lxml import etree

paste =  "http://pastebin.dapps.douban.com/"

code = sys.stdin.read()

payload = {
        'code':code,
        'language':'python'
        }

req = requests.post(paste, data=payload)
html = etree.HTML(req.text)

old = html.xpath('//input[@name="old"]')
id = old[0].xpath('.//@value')[0]

print "download at %sraw/%s/"%(paste, id)


