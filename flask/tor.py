#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
tor.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-11-25
'''

import tornado
import tornado.process
import tornado.web
import tornado.wsgi
from tornado import httpserver
from tornado import ioloop
from tornado.web import RequestHandler

class non(RequestHandler):
    def get(self):
        """docstring for get"""
        self.write("hello")
        
def main():
    """docstring for main"""
    print "@"
    #tornado.process.fork_processes(0)
    #sokets = tornado.netutil.bind_sockets(9993)
    application = tornado.web.Application([
        ('',non)])
    http_server = httpserver.HTTPServer(application)
    http_server.listen(9993)
    #http_server.add_sockets(sokets)
    ioloop.IOLoop.instance().start()

#application = tornado.wsgi.WSGIApplication([
#        ('/',non)])
if __name__ == '__main__':
    main()

