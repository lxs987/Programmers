# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:28:34 2022

@author: Jinkyung
"""

def solution(numbers, target):
    # tree 초기화
    tree = [0]
    # input으로 주어진 모든 number 리스트의 요소 순회
    for i in numbers:
        sub = []
        # tree에 저장된 모든 요소에 +i, -i하여 sub에 저장
        for j in tree: 
            sub.append(j+i)
            sub.append(j-i)
        # tree를 sub로 초기화
        tree = sub
    # tree에 저장된 모든 경우의 수가 저장된 연산 결과에서 target값을 count
    return tree.count(target)
