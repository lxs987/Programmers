# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 20:45:37 2022

@author: Jinkyung
"""

def solution(brown, yellow):
    # 전체 카펫의 칸
    total = brown + yellow
    # total에서 -1 해가면서 나눠지는지 확인
    # 나눠지면 가로길이 될 수 있음
    for width in range(total, 2, -1):
        if total % width == 0:
            # 전체를 가로로 나눈 값을 높이로 저장
            height = total // width
            # 가로와 세로에서 각각 -2 했을때의 넓이가 input yellow와 같다면 정답
            if yellow == (width-2)*(height-2):
                return [width, height]
