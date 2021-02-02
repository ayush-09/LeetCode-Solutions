# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:48:26 2021

@author: ayush
"""

def searchRange(nums, target):
    for i in range(len(nums)):
        if nums[i]==target:
            l=i
            break
    else:
        return [-1,-1]
    for j in range(len(nums)-1,-1,-1):
        if nums[j]==target:
            r=j
            break
    return [l,r]
print(searchRange([5,7,7,8,8,10],8))