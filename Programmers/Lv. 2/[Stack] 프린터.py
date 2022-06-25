# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 19:43:14 2022

@author: Jinkyung
"""

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
# 초기 풀이
# from collections import deque
# def solution(priorities, location):
#     answer = 0
#     # enumerate() 함수는 인자로 넘어온 목록을 기준으로 인덱스와 원소를 차례대로 접근하게 해주는 반복자(iterator) 객체를 반환해주는 함수
#     d = deque([(v, i) for i, v in enumerate(priorities)])
    
#     while len(d):
#         item = d.popleft()
#         if d and max(d)[0] > item[0]:
#             d.append(item)
#         else:
#             answer+=1
#             if item[1] == location:
#                 break
#     return answer
