# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 20:50:26 2022

@author: Jinkyung
"""

def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    sum = 0
    for i in range(len(A)):
        sum += A[i]*B[i]
    return sum
