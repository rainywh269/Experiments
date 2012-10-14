#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A(object):
    """docstring for A"""
    B= 1
    def __init__(self, arg=B):
        self.arg = arg
        

def main():
    print A().arg

if __name__ == '__main__':
    main()
