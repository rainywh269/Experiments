#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
from flask import Flask, url_for, request
import time

import re
app = Flask(__name__)

@app.before_request
def profile():
    request.start_time = time.time()

@app.after_request
def end(response):
    raise


@app.route("/")
def hello():
    page = urllib.urlopen("http://movie.douban.com/subject/10574468/mobile")
    found  =re.find_all('name="ck" value="(.*?)"', page)
    print found

    return str(request.start_time)
    return "Hello World!"

@app.route("/index")
def index():
    return "index"

if __name__ == "__main__":
    with app.test_request_context():
        print url_for('index')

    app.run(debug=True)
