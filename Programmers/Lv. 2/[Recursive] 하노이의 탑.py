# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 15:33:52 2022

@author: Jinkyung
"""

def solution(n):
    answer = hanoi(n,1,3,2)  
    return answer

def hanoi(n, start, end, bypass):
    if n == 1:
        return [[start, end]]
    else:
        path = []
        path += hanoi(n-1, start, bypass, end)
        path += [[start, end]]
        path += hanoi(n-1, bypass, end, start)
        
        return path
