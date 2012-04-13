#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import  Flask,request,redirect, url_for
from mako.template import Template
from model import Vote
import wtforms


app = Flask(__name__)

def get_form(model):
    class Builder(wtforms.form.FormMeta):
        def __new__(cls, name, bases, attrs):
            for k,v in model.__dict__.iteritems():
                if not k.startswith('_'):
                    attrs[k] = wtforms.TextField()
            new_cls = super(Builder,cls).__new__(cls,name,bases,attrs)
            return new_cls

    class form(wtforms.Form):
        __metaclass__ = Builder

    return form()

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
            #yield "FFFF"
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
        form = get_form(Vote)
        #form = SimpleForm()
        return render_form(form)
        return template.render(**locals())

if __name__ == '__main__':
    app.debug=True
    app.run()
