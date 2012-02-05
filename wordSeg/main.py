#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
main.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-11-13
'''

import mmseg
import mmseg.search

f = open('text')
dic = {}
for word in mmseg.seg_txt(f.read()):
    if word in dic.keys():
        dic[word] = int(dic[word] + 1)
    else:
        dic[word] = 1
f.close()

import operator
word = sorted(dic.iteritems(), key=operator.itemgetter(1),reverse=True)
print word
f = open('word','w')
f.writelines([str(k)+":"+str(v)+"\n" for (k,v) in word])
f.close()
