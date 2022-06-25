# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 18:41:24 2022

@author: Jinkyung
"""

def solution(n, a, b):
    cnt = 0
    while a != b:
        a, b = (a+1)//2, (b+1)//2
        cnt += 1
    return cnt

        # print("a: {0}, b: {1}".format(a, b))
        # 	a: 2, b: 4
        #   a: 1, b: 2
        #   a: 1, b: 1
