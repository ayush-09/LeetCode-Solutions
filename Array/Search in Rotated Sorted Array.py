# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:37:44 2021

@author: ayush
"""
def search(nums, target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    else:
        return -1
print(search([4,5,6,7,0,1,2], 0))