# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 21:06:56 2018

@author: deepak
"""

a=int(input("Enter number: "))
k=0
for i in range(2,a//2+1):
    if(a%i==0):
        k=k+1
if(k<=0):
    print("Number is prime")
else:
    print("Number isn't prime")