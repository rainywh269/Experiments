#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gevent import monkey;
monkey.patch_all()

from bottle import Bottle, run, get, post, request, response, static_file
from mako.template import Template
from os import path
from time import sleep

app = Bottle()

@app.get('/')
def get():
    #yield "Hello"
    #sleep(3)
    #yield "WORLD"
    #sleep(1)
    #yield "YOU"
    return Template(filename='template/index.html').render()


@app.post('/')
def post():
    data = request.files.f1
    #response.set_cookie(main
    raw =  data.file.read()
    filename = path.join('media/',data.filename)
    with open(filename,'w') as f:
        f.write(raw)
    return static_file(filename,root='.')

def main():
    run(app=app, server='gevent',reloader=True )

if __name__ == '__main__':
    main()

