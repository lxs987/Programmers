# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 19:08:21 2022

@author: Jinkyung
"""

def solution(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)          # stack이 비어있다면 push()
        else:
            if i == stack[-1]:       # stack 마지막 값과 s[i]가 같다면 pop()
                stack.pop()
            else:
                stack.append(i)      # stack 마지막 값과 s[i]가 다르면 push()

    if stack : return 0                 # stack이 비어있지 않다면 return 0
    else : return 1                     # stack이 비어있다면 return 1
