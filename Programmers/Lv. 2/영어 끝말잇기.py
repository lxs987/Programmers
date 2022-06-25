# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 18:57:04 2022

@author: Jinkyung
"""

def solution(n, words):
    # said: 말한 단어를 append하는 리스트
    said = [words[0]]
    for i in range(1, len(words)):
        # 이전 단어의 마지막 글자로 시작하지 않거나 이미 말했던 단어라면
        # 해당 사람의 번호와 순서를 divmod로 구하여 return
        if words[i-1][-1] != words[i][0] or words[i] in said:
            seq, num = divmod(i, n)
            return([num+1, seq+1])
        # 조건에 걸리지 않을 경우 말한 단어를 said 리스트에 저장
        said.append(words[i])
    # 매 순서에 조건을 통과했을 경우 탈락되는 사람이 없으므로 [0, 0] 리턴
    return [0, 0]
