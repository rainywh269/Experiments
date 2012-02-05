#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
test.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-12-30
'''

import re

txt='''回答说卡上 http：//dasd http：//dsad
技术的 wrongUrl!http://dasdsa http:/sdasd
会撒谎看 ttp：//dasd http：//dsad'''

print re.sub(".*wrongUrl.*","",txt)
