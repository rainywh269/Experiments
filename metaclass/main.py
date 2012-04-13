#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Meta(type):
    def __new__(cls, name, bases, attrs):
        new_cls = super(Meta,cls).__new__(cls, name, bases, attrs)
        if hasattr(new_cls, 'keywords'):
            new_cls.keywords += ('1','2')
        return new_cls

class B(object):
    keywords = ('0',)
    __metaclass__= Meta
    
def main():
    print B().keywords

if __name__ == '__main__':
    main()
