# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:55:47 2022

@author: Jinkyung
"""

def solution(bridge_length, weight, truck_weights):
    q = [0] * bridge_length
    answer = 0
    while q:
        answer += 1  # 시작했으므로 1초씩 더함
        q.pop(0)  # 트럭이 지나감
        if truck_weights:
            # 다리에 있는 트럭의 무게와 대기 중인 트럭의 무게가 제한 무게보다 작거나 같다면
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))  # 다리에 트럭 올림
            else:
                q.append(0)  # 중량 초과면 트럭 안올림
    return answer
