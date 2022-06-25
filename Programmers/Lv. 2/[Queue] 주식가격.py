# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 19:18:21 2022

@author: Jinkyung
"""

from collections import deque

def solution(prices):
    # deque로 만들기
    queue = deque(prices)
    answer = []

    while queue:
        # prices의 첫 가격을 price에 저장
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            # 가격이 떨어지는순간 break하고 현재 sec을 answer에 append
            if q < price:
                break 
        answer.append(sec)        
    return answer
