# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:55:04 2021

@author: ayush
"""

def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
    arr=sorted(nums)
    return arr.index(target)
            
print(searchInsert([1,3,5,6], 5))