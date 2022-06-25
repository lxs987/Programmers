# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 16:45:14 2022

@author: Jinkyung
"""

def solution(clothes):
    cHash = dict()

    for _, clothType in clothes:
        # get()을 통해 hash에 현재 cloth의 clothType이 존재하는지 확인한다
        # 없다면 0을, 있다면 value를 불러온다
        # 불러온 값에 +1 한 후, 다시 해시에 저장한다
        cHash[clothType] = cHash.get(clothType, 0) + 1

    # 모든 경우의 수 구하기
    answer = 1
    for v in cHash.values():
        # 각각의 수에 '+1'을 해주는 것은, '선택하지 않음'을 포함시켜준 것이다.
        # 따라서 각 종류의 의상 갯수에 +1을 해서 곱해준다.
        answer *= (v+1)

    # 아무것도 입지 않는 경우를 제외한다.
    return answer - 1
