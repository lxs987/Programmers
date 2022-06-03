# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 19:22:17 2022

@author: Jinkyung
"""

SELECT NAME, COUNT(NAME) as COUNT
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) >= 2
ORDER BY NAME
