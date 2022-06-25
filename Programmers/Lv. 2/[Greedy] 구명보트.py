# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 20:55:45 2022

@author: Jinkyung
"""

def solution(people, limit):
    answer = 0
    people.sort()
    light, heavy = 0, len(people)-1

    # 가장 무거운 사람 + 가장 가벼운 사람 조합으로 태움
    while light <= heavy:
        # 턴 지날 때마다 보트 개수 +1
        answer += 1
        # 가장 무거운 사람과 가벼운 사람의 합이 limit보다 작거나 같을 경우
        # 둘 다 태울 수 있으므로 light, heavy index 모두 +1, -1
        if people[light] + people[heavy] <= limit:
            light += 1
        # 둘 다 태울 수 없을 경우 가장 무거운 사람의 인덱스만 -1
        heavy -= 1
    # 필요한 보트의 수 return
    return answer
