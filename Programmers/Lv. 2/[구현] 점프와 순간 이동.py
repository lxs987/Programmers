# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 20:13:21 2022

@author: Jinkyung
"""

def solution(n):
    ans = 0
    while n!=0:
        n, mod = divmod(n, 2)
        ans += mod
    return ans
