#!/usr/bin/env python
# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser
from urllib2 import urlopen
import urllib
import logging
import os
import re
from mako.template import Template
from email.mime.text import MIMEText
import smtplib, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
from email.mime.base import MIMEBase
from lxml import html
import oauth2 
import json
from pprint import pprint
from configs import *


try:
    with open("latest") as f:
        q = int(f.read().strip())
except Exception,err:
    q = 0

consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
token = oauth2.Token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
url = "http://api.tumblr.com"

client = oauth2.Client(consumer, token)
url = "http://api.tumblr.com/v2/user/dashboard?limit=200%s"%("&since_id=%s"%q if q else "")
resp, content =  client.request(url,"GET")
content = json.loads(content)
pprint(content, indent=4)

text = []
for post in content['response']['posts']:
    if post['type'] == 'text':
        tmp = '<p>%s</p>' % post['title']+'-----'+ post['body'] 
        text.append(tmp)
    elif post['type'] == 'quote':
        text.append(post['text'])
    if int(post['id']>q):
        q = int(post['id'])

with open("latest",'w') as f:
    f.write(str(q))

text = '====='.join(text)



text = html.fromstring(text)
text = text.text_content()

text = text.replace('-----','\n\r---------\n\r')
text = text.replace('=====','\n\r=========\n\r')
text = text.encode('utf8')
print text
print send_mail(SMTP_USERNAME, ["guohaochuan@kindle.com"],'sddd', 'asdfasdf', text)
