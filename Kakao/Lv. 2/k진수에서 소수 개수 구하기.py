# -*- coding: utf-8 -*-
"""
Created on Sun May 29 19:44:53 2022

@author: Jinkyung
"""

# 10진수 n을 k진수로 변환
def convert(n, k):
    converted = ''
    #divmod() 사용하여 몫, 나머지를 동시에 구함
    # string에 mod를 append한 후
    while n>0:
        n, mod = divmod(n, k)
        converted += str(mod)
    # while문이 종료되면 뒤집어서 리턴함(변환된 값)
    return converted[::-1]

def is_prime(x):
    if x == 1: return False
    #제곱근까지만 약수 구하여 판별
    for i in range(2, int(x**0.5)+1):
        # 약수가 존재할 경우 즉시 종료, false 리턴
        if x % i == 0: return False
    return True

def solution(n, k):
    # k진수 변환
    converted = convert(n, k)
    # 소수 count 할 변수
    cntPrime = 0
    # k진수로 변환된 값을 0을 기준으로 나누고, 이를 num이라 하였을 때
    for num in converted.split('0'):
        # num이 숫자이고 소수라면
        if num.isdigit() and is_prime(int(num)):
            # 소수 cnt ++
                cntPrime += 1
    return cntPrime
