#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
main.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2012-06-08
'''
class ClassName(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        self.arg = arg

    def __add__(self, arg):
        return self.__class__(self.arg+arg.arg)

class A(ClassName):
    pass
def main():
    a= A(12)
    b= A(123)
    print (a+b).__class__

if __name__ == '__main__':
    main()
