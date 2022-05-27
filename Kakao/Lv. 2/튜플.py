# -*- coding: utf-8 -*-
"""
Created on Fri May 27 18:44:24 2022

@author: Jinkyung
"""

def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')
    #print(s1) 출력 예시: ['2', '2,1', '2,1,3', '2,1,3,4']

    new_s = []
    for i in s1:
        new_s.append(i.split(','))
    
    new_s.sort(key = len)
    # print(new_s) ex. 	[['2'], ['2', '1'], ['2', '1', '3'], ['2', '1', '3', '4']]
    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer
