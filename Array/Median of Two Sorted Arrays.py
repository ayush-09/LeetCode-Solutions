# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:42:42 2021

@author: ayush
"""
import statistics as st
def findMedianSortedArrays(nums1, nums2):
    s=[]
    for i in nums1:
        s.append(i)
    for j in nums2:
        s.append(j)
    a=sorted(s)
    return st.median(a)
print(float(findMedianSortedArrays([],[1])))