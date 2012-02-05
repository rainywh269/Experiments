#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
test.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-12-29
'''

import Queue
import os
import multiprocessing
import threading
import time

q = Queue.Queue()

def word():
    while not q.empty():
        print q.get()
        time.sleep(1)

def main():
    for x in range(100):
        q.put(x)
    
    pool = []
    for x in range(10):
        pool.append(threading.Thread(target=word))

    for x in pool:
        x.start()



if __name__ == '__main__':
    main()
