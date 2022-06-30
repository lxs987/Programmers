# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 17:56:41 2022

@author: Jinkyung
"""

from math import gcd

def solution(arr):
    answer = arr[0]
    for num in arr:
        # 리스트의 모든 요소를 돌면서 최소공배수를 구하여 저장함
        answer = answer*num // gcd(answer, num)
    return answer
