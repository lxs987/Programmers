# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 16:52:07 2022

@author: Jinkyung
"""
# 기본 원리: 피보나치
def solution(n):
    # dp 리스트 0으로 초기화
    dp = [0 for i in range(n)]
    # 초기값 설정
    dp[0] = 1
    dp[1] = 2
    # n이 3 이상일 때 가능한 타일 배치는
    #dp[3] = dp[2] + dp[1]로 표현할 수 있다.
    for i in range(2, n):
        fibo = dp[i-1] + dp[i-2]
        dp[i] = fibo % 1000000007
    return dp[n-1]
