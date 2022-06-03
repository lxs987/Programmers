# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 19:28:30 2022

@author: Jinkyung
"""

SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID
