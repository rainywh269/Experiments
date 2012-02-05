#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__init__.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-11-19
'''

import mako.lookup
import os
import sys
from os.path import abspath,dirname,join
from private_config import CONNECTION_STRING

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = 8080
URL_HANDLERS = []
UPLOAD_PATH = join(ROOT_PATH,"static/upload")

TEMPLATE_LOOKER = mako.lookup.TemplateLookup([ROOT_PATH+'/static'])

DATABASE_TABLES = { 'main': ['hello','*'] }
DATABASE_CONNECTION = 
DATABASE_CONFIG = {
        "main": {
            "master": DATABASE_CONNECTION,
            "tables": DATABASE_TABLES['main'],
            },
        }

@classmethod
def render(cl,template_name=None,**kargs):
    template = None
    if template_name:
        template = TEMPLATE_LOOKER.get_template(template_name)
    else:
        template = TEMPLATE_LOOKER.get_template(cl.__name__)
    if template:
        return template.render(**kargs)
