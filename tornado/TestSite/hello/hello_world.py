#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
hello_world.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-11-19
'''

from _url import addHandlers  
from _base import baseHandler
from model.h import Hello
from config import UPLOAD_PATH 
import os

@addHandlers(r'^/')
class rootIndex(baseHandler):
    def get(self):
        #new = Hello()
        #new.save()
        #new.commit()
        q = Hello.mc_get_list([1,2,3,4,5])
        self.write(self.render(items=q))

@addHandlers(r'/this')
class Upload(baseHandler):
    def post(self):
        file = self.request.files['file1']
        f = open(os.path.join(UPLOAD_PATH,file[0]['filename']),'w')
        f.write(file[0]['body'])
        f.flush()
        
    def get(self):
        self.finish('''
<html><body><form action="/this" method="POST" enctype="multipart/form-data">
<input type="file" name="file1">
<input type="submit" value="ok">
</form></body></html>''')
