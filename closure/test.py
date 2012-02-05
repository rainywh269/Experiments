#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
test.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-12-26
'''

def main():
    i=1
    t={}
    def _():
        t[i]=i
        i+=1
    for x in xrange(100):
        _()

    print t
        

if __name__ == '__main__':
    main()
