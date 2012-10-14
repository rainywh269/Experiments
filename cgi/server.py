#!/usr/bin/env python
  
  
import cgitb
  
cgitb.enable()
  
import time
  
print "Content-type: text/html"  
  
print #这行必须要!
  
print time.strftime('%Y-%m-%d %X', time.localtime() )
  
