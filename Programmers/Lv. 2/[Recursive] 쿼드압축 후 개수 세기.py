# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 15:27:58 2022

@author: Jinkyung
"""

def solution(arr):
    answer = [0, 0]
    N = len(arr)

    def compression(x, y, n):
        init = arr[x][y]  # 해당 네모값중 하나
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != init:  # 한번이라도 다르면 그 네모는 압축불가
                    nn = n // 2
                    compression(x, y, nn)
                    compression(x, y + nn, nn)
                    compression(x + nn, y, nn)
                    compression(x + nn, y + nn, nn)
                    return

        # 모두 통과했다면 압축가능
        answer[init] += 1

    compression(0, 0, N)
    return answer
