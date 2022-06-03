# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 19:09:39 2022

@author: Jinkyung
"""

from itertools import combinations_with_replacement
from collections import Counter
# 라이언이 쏠 수 있는 화살의 모든 조합을 돌면서 조건에 맞는지 확인하기
# 이럴 경우 0~10의 값으로 중복조합으로 n개를 뽑는 것
def solution(n, info):
    max_diff, max_comb_cnt = 0, {}

    for comb in combinations_with_replacement(range(11), n):
        cnt = Counter(comb)
        score1, score2 = 0, 0
        for i in range(1, 11):
            if info[10-i] < cnt[i]:
                score1 += i
            elif info[10-i] > 0:
                score2 += i
                
        diff = score1 - score2
        if diff > max_diff:
            max_comb_cnt = cnt
            max_diff = diff
            
    if max_diff > 0:
        answer = [0]*11
        for n in max_comb_cnt:
            answer[10-n] = max_comb_cnt[n] 
        return answer 
    else:
        return [-1]
