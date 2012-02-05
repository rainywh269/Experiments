#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time

chaging = 'No'
sema = threading.RLock()

class aFunc(threading.Thread):
    def __init__(self,para):
        threading.Thread.__init__(self)
        self.para = para

    def run(self):
        with sema:
            global chaging
            print self.para,"processing"
            time.sleep(5)
            chaging = self.para
            print self.para,"End"


if __name__ == '__main__':
    aThread = aFunc('aThread')
    aThread.start()

    bThread = aFunc('bThread')
    bThread.start()

    while True:
        time.sleep(1)
        print "chaging",chaging
