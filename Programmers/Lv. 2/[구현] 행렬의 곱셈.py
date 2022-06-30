# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 20:56:45 2022

@author: Jinkyung
"""

import numpy as np

def solution(arr1, arr2):
    # numpy.dot은 numpy array를 곱할 때 사용됨
    # tolist() 사용하여 list로 반환
    answer = np.dot(arr1, arr2).tolist()
    return answer
