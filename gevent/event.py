#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gevent
import gevent.event

lock = gevent.event.Event()
import time

def lock_wait():
    while 1:
        print 'waiting'
        lock.wait()
        print "god"

def clear():
    while 1:
        gevent.sleep(1)
        if not lock.is_set():
            lock.set()
            print "lock"
        else:
            lock.clear()
            print "free"

jobs = [gevent.spawn(clear)]
jobs += [gevent.spawn(lock_wait) for i in range(10)]
gevent.joinall(jobs)
