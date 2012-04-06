#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
dict_size.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2012-03-25
'''
import sys
frsys.getsizeof(a)om itertools import izip
def main():
    b=10000000
    old_size = 0
    for i in range(0,100,10):
        b = 2**i
        a = dict([m for m in izip(xrange(b),xrange(b))])
        print i,b, sys.getsizeof(a), old_size*(2**10)-sys.getsizeof(a)
        old_size = sys.getsizeof(a)


if __name__ == '__main__':
    main()
