# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 16:08:16 2022

@author: Jinkyung
"""

def solution(numbers):
    answer = []

    for number in numbers:
        # 2진수로 바꿔준 후 편의를 위해 앞에 0 붙임
        bin_number = list('0' + bin(number)[2:])
        # 2진수로 바꾼 수에서 '0'의 위치를 찾아 idx에 저장.
        # find(): 왼쪽부터, rfind(): 오른쪽부터 탐색
        idx = ''.join(bin_number).rfind('0')
        # 맨 오른쪽의 0을 1로 바꿔줌 (number가 짝수라면 작업 완료)
        bin_number[idx] = '1'

        # number가 홀수라면 idx+1 위치를 0으로 바꿈.
        # 예를 들어 7이라면 0111 -> 1111 -> 1011
        if number % 2 == 1:
            bin_number[idx+1] = '0'

        # 결과를 answer 리스트에 append (int(num, 2)를 해주어 2진수를 10진수로 변환)
        answer.append(int(''.join(bin_number), 2))

    return answer
