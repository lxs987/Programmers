# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 12:48:44 2022

@author: Jinkyung
"""

def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1):
        answer.append(max(divmod(i, n)) + 1)

    return answer
