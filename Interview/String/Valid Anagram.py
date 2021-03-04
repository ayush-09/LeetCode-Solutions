# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 12:50:18 2021

@author: ayush
"""
def isAnagram(s, t):
    l1=len(s)
    l2=len(t)
    if l1!=l2:
        return False
    s=sorted(s)
    t=sorted(t)
        # if t in s:
        #     return True
        # return False
    for i in range(l1):
        if s[i]!=t[i]:
            return False
    return True
print(isAnagram("anagram", "nagaram"))