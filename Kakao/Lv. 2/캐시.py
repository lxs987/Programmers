# -*- coding: utf-8 -*-
"""
Created on Fri May 27 18:45:21 2022

@author: Jinkyung
"""

def solution(cacheSize, cities):
    execTime = 0
    cache = []
    # 캐시가 없을 경우
    if cacheSize == 0:
        return len(cities)*5
    
    for city in cities:
        # cache hit
        if city.lower() in cache:
            cache.remove(city.lower())
            cache.append(city.lower()) # 해당 city를 리스트 마지막으로 보냄
            execTime += 1 # miss일 경우 실행시간 +1
        # cache miss
        else:
            if len(cache) == cacheSize: cache.pop(0) # LRU 알고리즘
            cache.append(city.lower())
            execTime += 5 # miss일 경우 실행시간 +5
    return execTime

# def solution(cacheSize, cities):
#     import collections
#     cache = collections.deque(maxlen=cacheSize)
#     time = 0
#     for i in cities:
#         s = i.lower()
#         if s in cache:
#             cache.remove(s)
#             cache.append(s)
#             time += 1
#         else:
#             cache.append(s)
#             time += 5
#     return time
