# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:38:05 2021

@author: ayush
"""
s="Marge, let's \"[went].\" I await {news} telegram"
def isPalindrome(s):
       d="!@#$%^&*()_-+=:;,./ {}'\""
       for i in d:
           s=s.replace(i, "")
       a=s.lower()
       r=a[::-1]
       print(a)
       print(r)
       if a==r:
           return True
       else:
           return False
print(isPalindrome(s))