# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 17:21:01 2022

@author: Jinkyung
"""

def solution(begin, end):
    answer = []
    MAX = 10000000
    for num in range(begin, end + 1):
        if num == 1:
            answer.append(0)
            continue
        else:
            start = 2 if num % 2 == 0 else 3
            answer.append(1)
            # 해당 n을 나누어 떨어지게 할 수 있는 값 중 가장 큰 값
            # 가장 작은 약수값으로 n을 나누었을 때의 몫
            for i in range(start, int(num ** 0.5) + 1):
                if num != i and num % i == 0:
                    if num // i <= MAX:
                        answer[-1] = num // i
                        break
    return answer
