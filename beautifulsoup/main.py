#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
import urllib2

response = urllib2.urlopen('http://www.databaseolympics.com/sport/sportevent.htm?sp=FEN&enum=130')
html = response.read()
soup = BeautifulSoup(html)

g = open('fencing_medalists.csv','w"')
t = soup.findAll("table", {'class' : 'pt8'})

for table in t:
    rows = table.findAll('tr')
    for tr in rows:
        cols = tr.findAll('td')
        for td in cols:
            theText=str(td.find(text=True))
            #theText=str(td.find(text=True)).encode("utf-8")
            if theText!="None":
                g.write(theText)
            else: 
                g.write("")
            g.write(",")
        g.write("\n")
