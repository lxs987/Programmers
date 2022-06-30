# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 19:35:55 2022

@author: Jinkyung
"""

def solution(board):
    n = len(board) 
    m = len(board[0])
    
    # 2중 포문으로 연산
    for i in range(1, n):
        for j in range(1, m):
            # 해당 위치의 값이 1일 경우
            if board[i][j] == 1:
                # ↖ ← ↓ 위치의 값이 모두 1이라면 해당 위치에 +1 (가장 큰 정사각형 +1)
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
    
    # 최대 넓이 구하기
    answer = 0
    for i in range(n):
        temp = max(board[i])
        answer = max(answer, temp)
    
    return answer**2
