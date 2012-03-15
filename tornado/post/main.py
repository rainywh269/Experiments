#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web 
import tornado.httpserver
from tornado.ioloop import IOLoop
from mako.template import Template


class Index(tornado.web.RequestHandler):
    def get(self):
        self.write(Template(text=open('index.html').read()).render())
    def post(self):
        x=self.get_argument('txt1')
        x+=self.get_argument('txt2')
        return self.write(x)

app = tornado.web.Application([
    ('/i.*',Index),
    ], debug=True )


def main():
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8080)
    IOLoop().instance().start()
    

if __name__ == '__main__':
    main()
