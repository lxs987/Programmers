# -*- coding: utf-8 -*-
"""
Created on Thu May 26 14:02:58 2022

@author: Jinkyung
"""

def solution(N, stages):
    result = {}
    total = len(stages)
    for stage in range(1, N+1):
        if total != 0:
            count = stages.count(stage)
            result[stage] = count/total
            total -= count
        else:
            result[stage]=0
    return sorted(result, key=lambda x: result[x], reverse=True)