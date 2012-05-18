#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
setsid.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2012-05-15
'''

import os
import sys
import time
import threading

class thread(threading.Thread):
    def run(self):
        while 1:
            time.sleep(0.3)
            print "alive", os.getpid()

def main():
    thread().start()
    print "!"
    pid = os.fork()
    time.sleep(3)
    if pid > 0:
        sys.exit(0)
    print 1
    time.sleep(3)

if __name__ == '__main__':
    main()
