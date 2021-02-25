# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:58:06 2021

@author: ayush
"""

a=[0,2,1,-6,6,7,9,-1,2,0,1]
m=3
def threeSubParts(a,m):
    summ=sum(a)
    if summ%m!=0:
        return "False"
    p=0
    t=0
    ide=summ//m
    for i in a:
        t=t+i
        if t==ide:
            t=0
            p+=1
    if p>=m:return "True"
    return "False"

print(threeSubParts(a, m))