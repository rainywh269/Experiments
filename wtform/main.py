#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import  Flask
from mako.template import Template
import wtforms
app = Flask(__name__)

class SimpleForm(wtforms.Form):
    user = wtforms.TextField("Username")
    password = wtforms.PasswordField("password")

@app.route("/")
def index():
    template = Template('''${name}''')
    form = SimpleForm()
    name = form.user
    return template.render(**locals())


if __name__ == '__main__':
    app.debug=True
    app.run()
