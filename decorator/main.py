#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Decorator(object):
    record = []
    @classmethod
    def __call__(cls,func):
        def _(*args):
            print "Old", cls.record
            cls.record+=args
            print "adding",args
        return _

def decorator(f):
    f.func_globals.update({"test1":"testSTR"})
    return f




@decorator
def test(arg1, arg2):
    print test1


def main():
    test("1","2")

if __name__ == '__main__':
    main()
print globals()
