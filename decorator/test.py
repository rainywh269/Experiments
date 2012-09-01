#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
test.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2012-01-11
'''

def func_1(func):
    print "!!!", func.__name__
    def _(a):
        print a,'this'
    return _

@func_1
def func2(a):
    print "2"


def main():
    func2('222')

if __name__ == '__main__':
    main()
