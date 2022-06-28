# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 17:31:47 2022

@author: Jinkyung
"""

def solution(skill, skill_trees):
    # answer에 skill_trees의 갯수 저장
    answer = len(skill_trees)
    for skill_tree in skill_trees:
        i = 0
        for s in skill_tree:
            # 현재 스킬이 skill에 있지만
            if s in skill:
                # 순서가 맞지 않다면
                if s != skill[i]:
                    # 가능하지 않은 스킬트리이므로 answer에서 1 빼고 break
                    answer-=1
                    break
                # 비교할 skill 인덱스에 +=1
                i += 1
    return answer
