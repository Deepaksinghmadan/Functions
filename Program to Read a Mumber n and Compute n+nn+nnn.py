# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 01:25:48 2017

@author: deepak
"""
a = int(input("enter the number of units you want"))
b = input("Enter the digit")
ans = str(0)
z = 0
for i in range(1,a+1):
    for j in range(1):
        ans=b+ans
    z = int(ans)+int(z)
print("Ans is"+" "+str(z))
