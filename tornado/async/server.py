#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado import web
from tornado import httpserver
from tornado import ioloop
from time import sleep
from random import random
import uuid


class MessageMixin(object):
    handlers = []
    members  = set()
    def wait_for_message(self,handler):
        print "adding", MessageMixin.members
        MessageMixin.members.add(handler)

    def new_message(self,txt):
        print MessageMixin.members
        for member in MessageMixin.members:
            print "calling"
            member(txt)
        MessageMixin.members=set()

class NewMessage(web.RequestHandler,MessageMixin):
    def get(self):
        self.new_message(str(random()))

class Index(web.RequestHandler,MessageMixin):
    @web.asynchronous
    def get(self):
        self.write(str(random()))
        self.flush()
        self.wait_for_message(self.on_new_info)

    def on_new_info(self,txt):
        if self.request.connection.stream.closed():
            return
        self.finish(txt)

class Index_Redirect(web.RequestHandler,MessageMixin):
    def get(self):
        self.redirect('/listen/%s'%uuid.uuid4())

app = web.Application([
    ('/',Index_Redirect),
    ('/new',NewMessage),
    ('/listen/.*', Index),
    ], debug=True)

def main():
    server = httpserver.HTTPServer(app)
    server.listen(8080)
    ioloop.IOLoop().instance().start()


if __name__ == '__main__':
    main()
