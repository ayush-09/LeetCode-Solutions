# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 12:45:04 2021

@author: ayush
"""

def distributeCandies(candyType):
    l = len(candyType)//2
    s = len(set(candyType))
    return min(l,s)

print(distributeCandies([1,1,2,3]))