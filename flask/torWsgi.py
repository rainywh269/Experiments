#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
torWsgi.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-11-25
'''

import tornado.web
import tornado.wsgi
import wsgiref.handlers

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.wsgi.WSGIApplication([
    (r"/", MainHandler),
])
