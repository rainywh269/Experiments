#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
notify.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-10-31
'''
import gtk,pynotify
import urllib2
import difflib
import time
import os
from time import gmtime,strftime
pynotify.init("this")
r = urllib2.urlopen('http://rainywh269.info/')
text =  r.read().strip()

while 1:
    r = urllib2.urlopen('http://rainywh269.info/')
    newText = r.read().strip()
    result = difflib.SequenceMatcher(None,text,newText).ratio()
    if result<0.9:
        n = pynotify.Notification("!!!!","new!!!")
        n.show()
        os.system('mplayer /usr/share/hotot/sound/notify.wav')
    else:
        print str(result) + "nothing changed" + strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    time.sleep(30)
    
