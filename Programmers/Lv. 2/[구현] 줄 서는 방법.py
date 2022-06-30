# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 19:19:14 2022

@author: Jinkyung
"""

import math

def solution(n, k):
    k -= 1
    answer = []
    numbers = list(range(1, n+1))
    
    for i in range(n, 0, -1):
        div, k = divmod(k, math.factorial(i-1))
        answer.append(numbers.pop(div))
        
    return answer
