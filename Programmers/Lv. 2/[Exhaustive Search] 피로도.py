# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 15:39:14 2022

@author: Jinkyung
"""

from itertools import permutations

def solution(k, dungeons):
    answer = 0
    # 가능한 순열을 모두 구하고 순열을 순회하며 탐험 가능한 최대 던전 수를 return
    for permut in permutations(dungeons, len(dungeons)):
        hp = k
        count = 0
        for pm in permut:
            if hp >= pm[0]:
                hp -= pm[1]
                count += 1
        if count > answer:
            answer = count
    
    return answer
