#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import get,post,Bottle,run

def df():
    for i in range(100):
        yield str(i)

app = Bottle()
@app.get('/')

def home():
    return df()

run(app=app,host='wooparadog.xxx', reloader=True)
