#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
gevent.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-12-29
'''

import gevent

def main():
    dd = range(199)
    jobs = [gevent.spawn(lambda x=x: x*2) for x in dd]
    gevent.joinall(jobs)
    for j in jobs:
        print j.value
if __name__ == '__main__':
    main()
