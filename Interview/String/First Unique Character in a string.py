# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 12:01:20 2021

@author: ayush
"""

from collections import Counter 
def firstUniqChar(s):
    st=Counter(s)
    for i in s:
        if st[i]==1:
            return s.index(i)
    return -1
print(firstUniqChar("leetcode"))