# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 20:36:50 2022

@author: Jinkyung
"""
from collections import deque

def solution(maps):
    row, column = len(maps), len(maps[0])
    # # 상:(-1, 0), 하:(1, 0), 좌:(0, -1), 우:(0, 1)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0, 0))

    # queue가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        # 상하좌우 칸 확인하기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵을 벗어나지 않으면서, 벽이 아닐 때
            if 0 <= nx < row and 0 <= ny < column:
                # 처음 지나가는 길이면 거리 계산
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))

    # while문 종료
    # return 최단거리
    # 상대 진영에 도착할 수 없다면 return -1
    return maps[row - 1][column - 1] if maps[row - 1][column - 1] > 1 else -1
