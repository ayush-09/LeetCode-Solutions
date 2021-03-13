# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:35:39 2021

@author: ayush
"""

def plusOne(digits):
    n=len(digits)
    for i in reversed(range(n)):
        digits[i]+=1
        if digits[i]<10:
            return digits
        else:
            digits[i]=0
    if digits[0]==0:
        digits.insert(0,1)
    return digits

print(plusOne([1,2,3]))