#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
main.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-11-21
'''

import json
import codecs

f = codecs.open('100100.js','r','utf-8')
a = json.load(f,encoding='utf-8')

f = codecs.open('1.js','w','utf-8')
json.dump(a,f,ensure_ascii=False)
