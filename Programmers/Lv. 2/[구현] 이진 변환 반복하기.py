# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 20:01:14 2022

@author: Jinkyung
"""

def solution(s):
    # 변환 횟수, 제거된 0의 갯수
    convertCnt, deletedZero = 0, 0
    while s != '1':
        convertCnt += 1
        # '1'의 갯수 count
        cntOne = s.count('1')
        # 제거된 0의 갯수 구하기
        deletedZero += len(s) - cntOne
        # 0이 제거된 s를 이진수로 변환하여 s에 삽입
        s = bin(cntOne)[2:]
    return [convertCnt, deletedZero]
