# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 21:07:58 2022

@author: Jinkyung
"""

def solution(s):
    # 공백을 기준으로 나누어 리스트로 저장
    s = s.split(" ")
    for i in range(len(s)):
        # 첫글자는 대문자, 그 뒤 글자는 소문자
        s[i] = s[i][:1].upper() + s[i][1:].lower()
    # 리스트 요소를 하나의 문자열로 합치
    return ' '.join(s)
