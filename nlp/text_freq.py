#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
#import matplotlib
from nltk.book import text1

freq=nltk.FreqDist(text1)
freq.plot(50, cumulative=True)
import ipdb;ipdb.set_trace()
