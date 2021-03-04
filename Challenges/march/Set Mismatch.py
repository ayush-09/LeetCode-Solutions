# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 11:32:42 2021

@author: ayush
"""
from collections import Counter
def findErrorNums(nums):
    n=len(nums)
    r=0
    m=Counter(nums)
    for i in m:
        if m.get(i)>1:
            r=i
    s=n*(n+1)//2
    d= list(set(nums))
    s1=sum(d)
    m=s-s1
    return str(r),str(m)

print(findErrorNums([1,2,2,4]))