# -*- coding: utf-8 -*-
"""
Created on Thu May 26 14:02:28 2022

@author: Jinkyung
"""

def solution(numbers, hand):
    answer=[]
    key = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          ['*', 0, '#']]
    left = '*'
    right = '#'
    for i in numbers:
        if i in [1, 4, 7]:
            answer.append('L')
            left = i
        elif i in [3, 6, 9]:
            answer.append('R')
            right = i
        else:
            new_i=[(j,k) for j in range(len(key)) for k in range(len(key[j])) if key[j][k]==i]
            new_left = [(j,k) for j in range(len(key)) for k in range(len(key[j])) if key[j][k]==left]
            new_right = [(j,k) for j in range(len(key)) for k in range(len(key[j])) if key[j][k]==right]
            
            left_result = abs(int(new_i[0][0]) - int(new_left[0][0])) + abs(int(new_i[0][1]) - int(new_left[0][1]))
            right_result = abs(int(new_i[0][0]) - int(new_right[0][0])) + abs(int(new_i[0][1]) - int(new_right[0][1]))
            
            if left_result == right_result:
                if hand=='right':
                    answer.append('R')
                    right = i
                else:
                    answer.append('L')
                    left = i
            elif left_result < right_result:
                answer.append('L')
                left = i
            else:
                answer.append('R')
                right = i
                    
            
    return "".join(answer)