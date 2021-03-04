# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 13:00:53 2021

@author: ayush
"""

def longestCommonPrefix(strs):
    if not strs:
        return ""
    start_word = strs[0]
    for i in range(len(start_word)):
        for j in range(1, len(strs)):
            if i >= len(strs[j]):
                return start_word[:i]
            if strs[j][i] != start_word[i]:
                return start_word[:i]
    return start_word

print(longestCommonPrefix(["dog","racecar","car"]))