# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 19:45:54 2022

@author: Jinkyung
"""

def solution(land):
    # 2번째행부터 고려
    for i in range(1, len(land)):
        # 같은 열을 제외하고
        # 윗 행의 숫자를 더했을 때 가질 수 있는 최댓값을 해당 위치에 저장함
        for j in range(4):
            land[i][j] += max(land[i-1][k] for k in range(4) if k != j)
    
    return max(land[-1])
