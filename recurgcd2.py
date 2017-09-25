# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 01:24:13 2017

@author: deepak
"""

def gcd2(a, b):
    if (0 == a % b):
        # calculate s and t
        return b
    else:
        g, s, t = gcd2(b, a % b)
        # calculate new_s and new_t
        return g