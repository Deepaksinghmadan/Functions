# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 23:09:06 2017

@author: deepak
"""

def printMov(fm,to):
    print("Move from " + str(fm) + " to " + str(to))
    
    
def tower(a,fm,to,spare):
    if a==1:
        print("Move from " + str(fm) + " to " + str(to))
        
    else:
        tower(a-1,fm,spare,to)
        tower(1,fm,to,spare)
        tower(a-1,spare,to,fm)
        
print(tower(3,'P1','P2','P3'))
