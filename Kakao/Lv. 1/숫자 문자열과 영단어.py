# -*- coding: utf-8 -*-
"""
Created on Thu May 26 14:02:07 2022

@author: Jinkyung
"""

def solution(s):
    cardinal = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in cardinal:
        if i in s:
            s = s.replace(i, str(cardinal.index(i)))
        
    return int(s)