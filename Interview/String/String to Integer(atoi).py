# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 15:40:19 2021

@author: Ayush
"""

def myAtoi(s):
    r = 0
    si = 1
    re = False
    for i in s:
        if i.isdigit():
            if not re:
                re =True
            r = r*10 + int(i)
        else:
            if i==" " and not re:
                continue
            if i =="+" and not re:
                re = True
                si = 1
                continue
            if i =="-" and not re:
                re = True
                si=-1
                continue
            break
    r1 = r*si
    if r1> 2**31 - 1:
        r1= 2**31 - 1
    if r1< -2**31:
        r1 = -2**31
    return r1