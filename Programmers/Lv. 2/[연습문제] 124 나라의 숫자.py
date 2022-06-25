# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:22:54 2022

@author: Jinkyung
"""

# n이 3의 배수가 아니라면 3진법과 동일하게 3으로 나눈 나머지를 저장하고, n을 3으로 나눈 몫을 저장한다. 만약 n이 3의 배수라면 4를 추가하고, n을 3으로 나눈 몫에서 1을 뺀 값을 저장한다.
def solution(n):
    answer = ''
    while n:
        if n % 3:
            answer += str(n % 3)
            n //= 3
        else:
            answer += "4"
            n = n//3 - 1
    return answer[::-1]
