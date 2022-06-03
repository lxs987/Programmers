# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 19:21:52 2022

@author: Jinkyung
"""

SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE
