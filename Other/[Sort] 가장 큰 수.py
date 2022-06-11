# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 15:14:38 2022

@author: Jinkyung
"""

def solution(numbers):

    numbers = list(map(str, numbers))
    # lambda x : x * 3은 num 인자 각각의 문자열을 3번 반복한다는 뜻
    # numbers의 원소는 1,000 이하이므로 3자리로 맞춰놓고 비교하기 위함
    numbers.sort(key=lambda x: x * 3, reverse=True)
    # 모든 값이 0일 때 (ex. '000')를 처리하기 위해 int로 바꾼 후 str형 return
    return str(int(''.join(numbers)))
