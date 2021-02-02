# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:57:11 2021

@author: ayush
"""

def firstMissingPositive(nums):
    c=1
    s=set()
    for i in nums:
        if i not in s and i > 0:
            s.add(i)
    
    while True:
        if c not in s:
            return c
        else:
            c += 1

print(firstMissingPositive([1,2,0]))