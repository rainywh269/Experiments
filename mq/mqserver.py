#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
mqserver.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-11-14
'''

import beanstalkc
import pickle
from decorator import decorator

mq = None
FUNCDICT={}
QUEUE='wooparadog'

def producer(func, name=None):
    global FUNCDICT
    name = name or func.__name__
    FUNCDICT[name] = func
    def _(func,*args,**kwds):
        global mq
        if not mq:
            mq = beanstalkc.Connection('localhost',port=11300,parse_yaml=True)
        mq.use(QUEUE)
        s = pickle.dumps((name,args,kwds))
        print "putting"
        print FUNCDICT
        mq.put(s)
    return decorator(_,func)

def comsumer():
    global mq,FUNCDICT
    if not mq:
        mq = beanstalkc.Connection('localhost',port=11300,parse_yaml=True)
    mq.use(QUEUE)
    mq.watch(QUEUE)
    while 1:
        try:
            print "getting"
            print FUNCDICT
            job = mq.reserve()
            name, args, kwds = pickle.loads(job.body)
            print name, args, kwds 
        except Exception as e:
            print e
            job.delete()
            continue
        print "calling"
        FUNCDICT[name](*args,**kwds)
        job.delete()

if __name__ == '__main__':
    comsumer()
