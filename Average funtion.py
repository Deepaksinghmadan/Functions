# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 00:39:12 2017

@author: deepak
"""

n = int(input("Enter the number of inputs"))
a=[]
for i in range(n):
    x = float(input("enter number"))
    a.append(x)
ans= sum(a)/n
print("Average of inputs are" ,round(ans,2))
