#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
testDictSetdefault.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-11-28
'''

import itertools
import operator
from collections import defaultdict

qrs = [{'type': 'a', 'data': 'hello'}, 
        {'type': 'b', 'data': 'hello1'}, 
        {'type': 'b', 'data': 'hello2'}, 
        {'type': 'b', 'data': 'hello3'}, 
        {'type': 'a', 'data': 'hello4'}, 
        {'type': 'a', 'data': 'hello5'}, 
        {'type': 'b', 'data': 'hello6'}, 
        {'type': 'b', 'data': 'hello7'}, 
        ]

tmp = qrs

def groupC():
    li=[]
    for i in qrs:
        for j in li:
            if 'type' in j:
                if i['type']==j['type']:
                    j['data'].append(i['data'])
            else:
                j=i
    print li

def group1():
    li=[]
    tmp.sort(key=operator.itemgetter('type'))
    for k,g in itertools.groupby(tmp,key=operator.itemgetter('type')):
        li.append({'type':k,'data':[i['data'] for i in g]})
    print li

def group2():
    d = defaultdict(list)
    [d[q['type']].append(q['data']) for q in qrs]
    result = [{'type': k, 'data': v} for k, v in d.items()]
    print result

def group3():
    new_list = {}
    for elem in qrs:
        new_list.setdefault(elem['type'], []).append(elem['data'])
    print new_list
    
if __name__ == '__main__':
    import cProfile
    cProfile.run('group1()')
    cProfile.run('group2()')
    cProfile.run('group3()')
