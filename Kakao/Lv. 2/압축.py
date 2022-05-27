# -*- coding: utf-8 -*-
"""
Created on Fri May 27 18:47:10 2022

@author: Jinkyung
"""

def solution(msg):
    # 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {k:v for (k,v) in zip(alphabet, list(range(1,27)))}
    answer = []

    while True:
        # 단어가 존재한다면 마지막글자 포함하여 answer에 추가
        if msg in d:
            answer.append(d[msg])
            break
        # msg의 길이를 키워가며 d에서 찾음
        for i in range(1, len(msg)+1):
            if msg[0:i] not in d:
                # 사전에 등록
                answer.append(d[msg[0:i-1]])
                # 사전에 없으므로 색인번호 출력
                d[msg[0:i]] = len(d)+1
                msg = msg[i-1:]
                break

    return answer
