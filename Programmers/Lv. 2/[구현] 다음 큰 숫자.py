# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 17:01:58 2022

@author: Jinkyung
"""

def solution(n):
    oriNum = str(bin(n)[2:]).count('1')
    i=1
    while n!=0:
        newNum = str(bin(n+i)[2:]).count('1')
        if oriNum == newNum:
            return n+i
        i+=1
