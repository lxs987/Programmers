# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 19:17:53 2022

@author: Jinkyung
"""

def solution(n):
    count = 0                      
    for i in range(1, n+1):         # n = n 고려하기 위해 n+1까지 구함
        sumN = 0                     
        for j in range(i, n+1):     # i값을 시작으로 반복문 실행
            sumN += j               # i값부터 계속해서 값을 더해준다
            if sumN == n:           # 더한 값이(sumN)이 n과 같다면 count +1, break
                count += 1          
                break
            if sumN > n:            # 더한 값(sumN)이 n보다 크다면 조건 충족 X
                break
    return count
