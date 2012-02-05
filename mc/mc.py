#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
mc.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-12-05
'''

import cmemcached

client = cmemcached.Client(['localhost:11211'])
client.set('this','hello')
print client.get('this')

if __name__ == '__main__':
    pass
