#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, url_for
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/index")
def index():
    return "index"

if __name__ == "__main__":
    with app.test_request_context():
        print url_for('index')

    #app.run(debug=True)
