#!/usr/bin/env python
# -*- coding: utf-8 -*-
def str2int(txt):
    str_dict = {
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
            }
    sign = ['+', '-', '.']
    endofsign = False
    endofpoiont = False
    positive = True
    val = 0
    multiplier = 10
    float_multiplier = 1
    negative_pos = 0
    for i in txt:
        if i not in str_dict and i not in sign:
            raise

        if not endofsign:
            if i == sign[1]:
                positive = not positive

        if i in str_dict:
            endofsign = True
            val *= multiplier
            val += str_dict[i]*(float_multiplier**negative_pos)
            if endofpoiont:
                negative_pos+=1

        if i == sign[2] :
            if endofpoiont:
                raise

            val = float(val)
            multiplier = 1
            float_multiplier = 0.1
            negative_pos = 1
            endofpoiont = True

    if not positive:
        val = -val

    return val
if __name__ == '__main__':
    print str2int('++++-00123.12')
    print str2int('++++---123.12')
    print str2int('1231..3.')
    print str2int('asdf')
    print str2int('123d')

