# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 20:21:48 2018

@author: deepak
"""

def bar():
    x = 10
    def spam(): # Nested function definition
        print ('x is', x)
    while x > 0:
        spam()
        x -= 1
        
bar()