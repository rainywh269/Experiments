#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 wooparadog <wooparadog@1l0v3U4v3r>
#
# Distributed under terms of the MIT license.

class PropsMixin(object):
    """docstring for PropsMixin"""
    def _props(self):
        return self.__props if hasattr(self, "__props") else {}

    def _props_setter(self, name, value):
        if hasattr(self, "__props"):
            self.__props.update(name=value)
        else:
            self.__props = {name:value}

class PropsItem(object):
    """docstring for PropsItem"""
    def __init__(self, name):
        super(PropsItem, self).__init__()
        self.name = name
        self.value = None

    def __set__(self, obj, value):
        print "!"
        obj._props_setter(self.name, value)

class MetaClass(type):
    """docstring for MetaClass"""
    def __new__(cls, name, bases, attrs):
        obj =  super(MetaClass, cls).__new__(cls, name, bases, attrs)

        

class A(PropsMixin):
    props = PropsItem("GOOGD")
    """docstring for A"""
    def __init__(self, arg):
        super(A, self).__init__()
        self.arg = arg

if __name__ == '__main__':
    a = A("1")
    a.props = 1

