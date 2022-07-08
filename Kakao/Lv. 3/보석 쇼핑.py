# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 01:13:47 2022

@author: Jinkyung
"""

def solution(gems):
    N = len(gems) # 보석의 총 갯수
    answer = [0, N-1] # answer는 전 구간으로 초기화
    kind = len(set(gems))  # 모든 보석의 종류
    dic = {gems[0]: 1}  # 종류 체크할 딕셔너리
    start, end = 0, 0  # 투포인터
    while start < N and end < N:
        if len(dic) < kind:  # 딕셔너리에 모든 종류의 보석이 추가되지 않았다면
            # end pointer += 1
            # 딕셔너리에 "해당 보석의 이름 : 1" 형식으로 추가
            end += 1
            if end == N:
                break
            dic[gems[end]] = dic.get(gems[end], 0) + 1
            # 예시) {EMERALD":3,"SAPPHIRE":1}

        else:   # 딕셔너리에 모든 종류의 보석이 담겨있을 경우
            if (end-start+1) < (answer[1]-answer[0]+1): # 현재 start~end 구간이 기존 start~end 구간보다 짧을 경우
                answer = [start, end]   # answer 업데이트
            if dic[gems[start]] == 1: # start 위치에 있는 보석이 하나밖에 없다면 해당 딕셔너리 값 아예 삭제
                del dic[gems[start]]
            else: # start 위치에 있는 보석이 2개 이상이라면 갯수 1개 차감
                dic[gems[start]] -= 1
            start += 1 # start index 1 증가

    # while문 종료되었을 때 최종적으로 업데이트 된 start, end 포인터 값에 +1 하여 리턴
    return [answer[0]+1, answer[1]+1]
