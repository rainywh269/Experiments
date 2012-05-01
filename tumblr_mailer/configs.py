#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
configs.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2012-05-01
'''

from os import path
current_path = path.dirname(path.abspath(__file__))
DB_FILENAME = "db.sqlite3"
DB_FILE = path.join(current_path, DB_FILENAME)

SMTP = 'smtp.mailgun.org'
SMTP_USERNAME = 'postmaster@wooparadog.mailgun.org'
SMTP_PASSWORD = '2zcpxlnii6x0'
SENDER_MAIL = SMTP_USERNAME

USER = "wooparadog"

CONSUMER_KEY = '8S8L87KTxFnDPyLxKeZ51902RMsKDsy0deUW20LExVJ7LJ5WiP'
CONSUMER_SECRET = 'nzqZqnmNg2RNKEuSAXRLS2gA45qi836lKD6IIJUxp9QaiFMHyA'
OAUTH_TOKEN = 'QB6OBdLOZH1TRXxOd1SzmMgw6ZQsIy0pqPVRrKDObzniYcAAqf'
OAUTH_TOKEN_SECRET = 'Wcz7bUDYksJiAqDF7rrTiSomDXgUhboEGUijWi35x9hSrzqjA5'
