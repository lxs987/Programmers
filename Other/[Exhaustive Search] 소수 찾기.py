# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 15:15:43 2022

@author: Jinkyung
"""

from itertools import permutations
import math

def is_prime(n):
    k = math.sqrt(n)
    if n < 2: 
        return False
    
    # 제곱근까지만 비교
    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    # 모든 길이의 순열 구하기
    for k in range(1, len(numbers)+1):
        per_list = list(map(''.join, permutations(list(numbers), k)))
        for i in list(set(per_list)):
            if is_prime(int(i)):
                answer.append(int(i))
    # 중복 제거
    return len(set(answer))
