# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 19:43:54 2022

@author: Jinkyung
"""

def dfs(i,j,k,field,grid):
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    cnt = 0
    row = len(grid)
    col = len(grid[0])
    
    while True:
        if field[i][j][k] == 1:
            return (cnt)
        
        field[i][j][k] = 1
        i = (i + dx[k]) % row
        j = (j + dy[k]) % col
        
        if grid[i][j] == 'R':
            k = (k + 1) % 4

        elif grid[i][j] == 'L':
            k = (k + 3) % 4
        
        cnt += 1

def solution(grid):
    answer = []
    row = len(grid)
    col = len(grid[0])
    field = [[[0,0,0,0] for i in range(col)] for j in range(row)]
    
    
    for i in range(row):
        for j in range(col):
            for k in range(4):
                if field[i][j][k] == 0:
                    answer.append(dfs(i,j,k,field,grid))
    answer.sort()
    
    return answer
