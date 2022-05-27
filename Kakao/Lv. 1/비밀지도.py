# -*- coding: utf-8 -*-
"""
Created on Thu May 26 14:03:20 2022

@author: Jinkyung
"""

def solution(n, arr1, arr2):
    answer = []
    b1=[]
    b2=[]
    for i in arr1:
        b1.append(str(format(i, 'b')).zfill(n))
    for i in arr2:
        b2.append(str(format(i, 'b')).zfill(n))
    
    for i in range(len(b1)):
        result = ""
        for j in range(len(b1)):
            if b1[i][j]==b2[i][j] and b1[i][j]=="0":
                result+=" "
            else:
                result+="#"
        answer.append(result)
    return answer
