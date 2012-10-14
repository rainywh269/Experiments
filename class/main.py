#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fun(a):
    def fun2():
        print a
    return fun

class ClassName(object):
    df = fun(1)
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg
        

def main():
    pass

if __name__ == '__main__':
    main()
