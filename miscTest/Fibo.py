#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Fibo.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-12-04
'''

def fibonacci():
    """a generator for Fibonacci numbers, goes to next number in series on each call"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fibonacci()
for x in range(10000):
    print f.next(),  # 0 1 1 2 3 5 8 13 21 34 55 89 144

#    
#def fibo(n):
#    """
#    use recursion to get Fibonacci numbers, returns the Fibonacci value for n
#    not very efficient because of the many function calls
#    """
#    if n < 2:
#        return n
#    else:
#        return fibo(n - 1) + fibo(n - 2)
#
#for x in range(13):
#    print "fibo(%d) = %d" % (x, fibo(x))
#    
#print
#print "Calculating ..."
#print
#
#print "fibo(%d) = %d" % (30, fibo(30))  # this takes a moment!
