# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:48:22 2021

@author: ayush
"""

def maxArea(height):
    l=len(height)
    if l==1 or l==0:
        return(0)
    elif l==2:
        return(min(height))
    else:
        result=[]
        l,r=0,l-1
        c=0
        while l<r:
            if height[l]<height[r]:
                a=height[l]*(r-l)
                c=max(a,c)
                l=l+1
            else:
                a=height[r]*(r-l)
                c=max(a,c)
                r=r-1
        return(c)
print(maxArea([1,1]))