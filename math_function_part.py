# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 13:09:29 2018

@author: Administrator
"""

def gcd(a, b):
    if a < b:
        a, b = b, a
    
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a