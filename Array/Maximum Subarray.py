# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:26:23 2021

@author: ayush
"""

def maxSubArray(nums):
    max_c=m=nums[0]
    for i in range(1, len(nums)):
        max_c = max(nums[i],max_c+nums[i])
        if max_c>m:
            m=max_c
    return m

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
        