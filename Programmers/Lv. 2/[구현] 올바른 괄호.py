# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 16:53:58 2022

@author: Jinkyung
"""

def solution(s):
    stack=[]
    for i in s:
        # 여는 괄호일 경우 stack에 적재하기
        if i == "(":
            stack.append(i)
        else:
            # stack이 비어있는 상태에서 닫는 괄호가 나오면 False
            if not stack:
                return False
            # 올바른 괄호인 경우 pop
            stack.pop()
    
    # stack이 비어있다면 올바른 괄호
    if not stack:
        return True
    else:
        return False
