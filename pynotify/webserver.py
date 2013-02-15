#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import tornado.httpserver
from tornado.ioloop import IOLoop
import tornado.websocket
from notifier import INotifyReloader

watched_dirs = (
        #"movie/static",
        #"static",
        #"fm/static",
        "movie/templates"
        ,
        )
static_refresher = INotifyReloader(watched_dirs, callback=lambda event:None)
static_refresher.start()

class I(tornado.websocket.WebSocketHandler):
    def open(self):
        print "open"
        self.write_message(">>>>")
    def on_message(self, message):
        print message
        self.write_message("BBB")
    def on_close(self):
        print "close"

app = tornado.web.Application([
    ('/notify',I),
    ], debug=True )

def main():
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8080)
    IOLoop().instance().start()

if __name__ == '__main__':
    main()
