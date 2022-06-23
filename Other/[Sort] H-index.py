# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 18:12:31 2022

@author: Jinkyung
"""

def solution(citations):
    # 인용 횟수 내림차순으로 정렬
    citations.sort(reverse=True)
    # index, 인용 횟수 for-loop
    for idx, citation in enumerate(citations):
        # index가 인용횟수보다 크거나 같다면 return index
        if idx >= citation:
            return idx
    # 모든 index가 인용횟수보다 작다면 인용횟수의 길이를 return
    return len(citations)
