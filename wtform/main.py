#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import  Flask,request,redirect, url_for
from mako.template import Template
import wtforms

app = Flask(__name__)

class SimpleForm(wtforms.Form):
    user = wtforms.TextField("Username")
    email = wtforms.TextField(validators=[wtforms.validators.Email()])
    password = wtforms.PasswordField("password")

def render_form(form):
    result = ['<form method="POST">']
    for i in form._fields.itervalues():
        result.append('%s : %s'%(i.label,i()))
    result.append('<input type="submit" value="OK" />')
    result.append('</form>')
    return '<br/>'.join(result)

@app.route("/",methods=["POST","GET"])
def index():
    if request.method=="POST":
        data = SimpleForm(request.form)
        if data.validate():
            return str(data.data)
        else:
            yield "FFFF"
            redirect(url_for(index))
    else:
        template = Template('''
        <form  method="POST">
                ${form.user.label}: ${form.user()} <br/>
                ${form.email.label}: ${form.email()}<br/>
                ${form.password.label}: ${form.password()}<br/>
               <input type="submit" value="" /> 
        </form>
                ''')
        form = SimpleForm()
        return render_form(form)
        return template.render(**locals())

if __name__ == '__main__':
    app.debug=True
    app.run()
