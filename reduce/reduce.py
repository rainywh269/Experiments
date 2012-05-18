#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
reduce.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2012-05-17
'''

a=[(1,2), (2,3), (3,6), (1,3), (2,1), (3,1)]
def reducer(v1,v2):
    if v1[0] == v2[0]:
        return (v1[0], v1[0]+v2[0])
    else:return v1, v2

a.sort(key=lambda x:x[0])
print reduce(reducer, a)
