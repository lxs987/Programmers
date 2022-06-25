# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 19:09:01 2022

@author: Jinkyung
"""

from math import gcd
def solution(width, height):
    answer = width * height - (width + height - gcd(width,height)) # = w*h - (w/g + h/g -1)*g
    return answer

# 초기 풀이
# def gcd(w, h):
#     if w%h == 0:
#         return h
#     else:
#         return gcd(h, w%h)

# def solution(w,h):
#     g = gcd(w,h)
#     answer = w*h - (w/g + h/g -1)*g
#     return answer
