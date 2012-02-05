#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
mqconsumer.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-11-14
'''

from mqserver import producer
from time import sleep

@producer
def aProducer(l,dic):
    sleep(1)
    print str(l),str(dic)

if __name__ == '__main__':
    for i in xrange(5):
        aProducer(str(i),{str(i):i})
