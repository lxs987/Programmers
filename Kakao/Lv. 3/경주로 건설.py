# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 16:15:02 2022

@author: Jinkyung
"""

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
INF = 25 * 25 * 600
answer = INF

def solution(board):
    dp = [[INF] * len(board) for _ in range(len(board))]

    def calcCost(x, y, n, cost, dir):
        global answer
        if dp[x][y] < cost:
            return
        else:
            dp[x][y] = cost

        # 종료조건
        if (x, y) == (n-1, n-1):
            if cost < answer:
                answer = cost
            return

        # 지나온 곳 마킹
        board[x][y] = -1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < n) and board[nx][ny] == 0:
                if(x, y) == (0, 0) or (dir+i) % 2 == 0:
                    calcCost(nx, ny, n, cost+100, i)
                else:
                    calcCost(nx, ny, n, cost+600, i)
        # 마킹 해제
        board[x][y] = 0

    #답 구하기
    calcCost(0, 0, len(board), 0, 0)
    return answer
