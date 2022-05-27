# -*- coding: utf-8 -*-
"""
Created on Fri May 27 18:43:09 2022

@author: Jinkyung
"""

def solution(orders, course):
        import itertools

        answer = []

        for size in course:
            order_dict = {}
            order_combinations = []
            for order in orders:
                #iterable중에서 r개를 선택할 수 있는 조합을 이터레이터로 리턴
                order_combinations.extend(list(itertools.combinations(sorted(order), size)))
            
            #print(order_combinations)
            for order_combination in order_combinations:
                order_str = ''.join(order_combination)
                if order_str in order_dict:
                    order_dict[order_str] += 1
                else:
                    order_dict[order_str] = 1
            #print(order_dict)
            
            for order in order_dict:
                if order_dict[order] == max([order_dict[order] for order in order_dict]):
                    if order_dict[order] > 1:
                        answer.append(order)


        return sorted(answer) # 오름차순으로 반환해야 하기 때문에, sorted로 정렬 해준다.
    
# 참고한 사이트: https://velog.io/@jwisgenius/프로그래머스-LV2-메뉴-리뉴얼
