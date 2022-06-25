# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 15:35:03 2022

@author: Jinkyung
"""

def solution(number, k):
    answer = []
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
        
    return ''.join(answer[:len(answer)-k])
