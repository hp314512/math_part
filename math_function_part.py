# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 13:09:29 2018

@author: Administrator
"""

#最大公约数，辗转相除法
def gcd(a, b):
    if a < b:
        a, b = b, a
    
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

#lcm = a*b/gcd,即两数乘积/最大公约数
def lcm(a, b):
    t = a*b
    if a < b:
        a, b = b, a
    
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return t/a