#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
server.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2012-05-09
'''

from gevent.pywsgi import WSGIServer

def application(environ, start_response):
    status = '200 OK'

    headers = [
        ('Content-Type', 'text/html')
    ]

    start_response(status, headers)
    yield "<p>Hello"
    yield "World</p>"

WSGIServer(('', 8000), application).serve_forever()
