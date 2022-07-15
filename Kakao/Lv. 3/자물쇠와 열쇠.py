# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 19:16:39 2022

@author: Jinkyung
"""

import copy
# 오른쪽으로 90도 회전
def rotate_key(M, key):
    new_key = [[0 for _ in range(M)] for _ in range(M)]
    for i in range(M):
        for j in range(M):
            new_key[i][j] = key[M-1-j][i]
    return new_key

# 자물쇠가 열렸는지 확인
def check(arr, N, M):
    for i in range(N):
        for j in range(N):
            if arr[M+i][M+j] != 1:
                return False
    return True

# 자물쇠와 키 맞는지 계산
def try_key(arr, key, N, M):
    # key로 자물쇠가 열리는지 확인
    for i in range(N+M):
        for j in range(N+M):
            # 값이 변경되므로 복사해서 사용
            cur_arr = copy.deepcopy(arr)
            for mi in range(M):
                for mj in range(M):
                    cur_arr[i+mi][j+mj] += key[mi][mj]

            if check(cur_arr, N, M):
                return True
    return False
def solution(key, lock):
    M = len(key)
    N = len(lock)
    L = 2*M+N
    
    # 키를 움직여가며 자물쇠와 맞혀볼 수 있는 판
    arr = [[0 for _ in range(L)] for _ in range(L)]
    
    # 중앙의 자물쇠를 배치
    for i in range(N):
        for j in range(N):
            arr[M+i][M+j] = lock[i][j]

    # key를 회전시켜서 자물쇠가 열리는지 확인
    for _ in range(4):
        if try_key(arr, key, N, M):
            return True
        key = rotate_key(M, key)
    return False
