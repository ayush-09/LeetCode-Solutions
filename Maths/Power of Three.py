# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 15:34:52 2021

@author: Ayush
"""

def isPowerOfThree(n):
        k=[3**i for i in range(100)]
        if n in k:
            return True
        else:
            return False
print(isPowerOfThree(27))