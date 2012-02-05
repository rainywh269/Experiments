#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
df.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-11-28
'''

import operator
import itertools
a = [(1,2),(2,3)]
print sum(itertools.imap(operator.itemgetter(1),a))
