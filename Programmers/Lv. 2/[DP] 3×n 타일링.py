# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 20:36:45 2022

@author: Jinkyung
"""

def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 1  # 아무것도 두지 않는 경우
    sub = 0
    for i in range(2, n + 1, 2):
        # sub * 2 를 더해주는 이유
        # 다음 단계로 진행할 때마다 아래와 같이 매번 2개씩 새로운 모양의 타일이 생긴다
        # 참고한 사이트: https://s2choco.tistory.com/24
        dp[i] = dp[i - 2] * 3 + sub * 2
        sub += dp[i - 2]

    return dp[n] % 1000000007
