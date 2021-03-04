# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 17:14:45 2021

@author: ayush
"""

def strStr(haystack, needle):
    if not needle:
        return 0
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

print(strStr("aaaaa", "bba"))