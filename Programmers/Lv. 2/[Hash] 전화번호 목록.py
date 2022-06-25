# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 19:57:09 2022

@author: Jinkyung
"""

# 간결하지만 효율성 좋지 않음
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
        
    return True

# Hash 사용하여 정석으로 푼 풀이
# def solution(phone_book):
#     answer = True
#     hash_map = {}
#     for phone_number in phone_book:
#         hash_map[phone_number] = 1
#     for phone_number in phone_book:
#         temp = ""
#         for number in phone_number:
#             temp += number
#             if temp in hash_map and temp != phone_number:
#                 answer = False
#     return answer
