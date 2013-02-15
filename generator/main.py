#!/usr/bin/env python
# -*- coding: utf-8 -*-

def consumer():
    while 1:
        data = yield
        if data:
            print data
    print "ended"

if __name__ == '__main__':
    target = consumer()
    target.next()
    target.send("23123")
