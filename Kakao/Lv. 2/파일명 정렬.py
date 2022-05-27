# -*- coding: utf-8 -*-
"""
Created on Fri May 27 18:47:21 2022

@author: Jinkyung
"""

import re
def solution(files): 
    # 입력된 files의 각 원소를 정규표현식 사용하여 숫자를 기준으로 나눔 
    temp = [re.split(r"([0-9]+)", s) for s in files]

    # temp를 정렬한 sort 리스트를 생성
    # 이 때, lambda식을 사용하여 HEAD를 1순위, NUMBER를 2순위로 하여 정렬한다.
    # 대문자와 소문자의 우선순위를 같게 하기 위해 lower()함수를 사용한다.
    sort = sorted(temp, key = lambda x: (x[0].lower(), int(x[1])))

    # split으로 쪼개졌던 각 원소를 다시 하나로 합친다.
    return [''.join(s) for s in sort]
