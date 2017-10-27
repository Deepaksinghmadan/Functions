# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 03:38:14 2017

@author: deepak
"""

n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)