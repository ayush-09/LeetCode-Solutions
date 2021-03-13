# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 19:41:48 2021

@author: ayush
"""

def removeDuplicates(nums):
    nums[:]=set(nums)
    nums.sort()
    return len(nums)
print(removeDuplicates([1,1,2]))