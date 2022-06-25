# -*- coding: utf-8 -*-
"""
Created on Tue May 31 13:43:31 2022

@author: Jinkyung
"""

import math

def solution(progresses, speeds):
    days = []
    answer = [1]

    # 각 작업이 끝나기까지 남은 일수 계산
    for i in range(len(speeds)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))

    init = days[0]

    for i in range(1, len(days)):
        if days[i] <= init:
            answer[-1] += 1
        else:
            answer.append(1)
            init = days[i]

    return answer
