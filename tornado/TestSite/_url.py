#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
_url.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-11-19
'''

URL_HANDLERS = []

def addHandlers(url):
    def _(cl):
        URL_HANDLERS.append((url,cl))
    return _
