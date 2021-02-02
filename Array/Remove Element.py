# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 19:48:23 2021

@author: ayush
"""

def removeElement(nums, val):
    while(val in nums):
        del nums[nums.index(val)]
    return len(nums)
print(removeElement([3,2,2,3], 3))