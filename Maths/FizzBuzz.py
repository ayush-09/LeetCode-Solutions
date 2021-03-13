# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 14:42:57 2021

@author: ayush
"""

def fizzBuzz(n):
    r=[]
    for i in range(1,n+1):
        if i%5==0 and i%3==0:
            r.append("FizzBuzz")
        elif i%5==0:
            r.append("Buzz")
        elif i%3==0:
            r.append("Fizz")
        else:
            r.append(str(i))
    return r

print(fizzBuzz(20))