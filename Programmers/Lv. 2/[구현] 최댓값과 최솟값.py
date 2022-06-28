# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 20:31:21 2022

@author: Jinkyung
"""

def solution(s):
    lst = list(map(int, s.split()))
    return "{0} {1}".format(min(lst), max(lst))
