# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 00:44:50 2017

@author: deepak
"""

def gcdIter(a, b):
    if (a<1 or b<1):
      print("No factor")
    elif a > b:
      for i in range(1,b+1):
          if (a%i==0 and b%i==0):
            GCD=i
      return(GCD)
    elif a <= b:
      for i in range(1,a+1):
        if (a%i==0 and b%i==0):
          GCD=i
      return(GCD)
    else:
       return("no factor")


