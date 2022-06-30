# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 20:51:04 2022

@author: Jinkyung
"""

def solution(n):
    dp = [i for i in range(n+2)]
    for i in range(4, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    
    return dp[n]%1234567
