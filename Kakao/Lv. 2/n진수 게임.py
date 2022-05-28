# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import string
# 숫자와 대문자를 tmp에 저장함
tmp = string.digits+string.ascii_uppercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

def solution(n, t, m, p):
    converted = ''
    answer = ''
    for i in range(t*m):
        converted += convert(i, n)
    for i in range(p-1, t*m, m):
        answer+=converted[i]
    return answer
