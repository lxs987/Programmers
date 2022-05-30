# -*- coding: utf-8 -*-
"""
Created on Mon May 30 20:43:43 2022

@author: Jinkyung
"""

import math

def solution(fees, records):
    dic = dict()
    result = dict()
    answer=[]
    
    for i in records:
        inputTime, carNum, status = i.split(' ')
        timeList = inputTime.split(':')
        timeSum = int(timeList[0])*60 + int(timeList[1])
        if status == 'IN':
            dic[str(carNum)] = timeSum
        else:
            if str(carNum) in result:
                result[str(carNum)] += timeSum - dic[str(carNum)]
            else:
                result[str(carNum)] = timeSum - dic[str(carNum)]
            del dic[str(carNum)]
            
    endTime = 23*60 + 59
    for carNum, time in dic.items():
        if carNum in result:
            result[carNum] += endTime - time
        else:
            result[carNum] = endTime - time
            
    sortedResult = dict(sorted(result.items(), key=lambda x:int(x[0])))
    
    for i in sortedResult.values():
        if i<=fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((i-fees[0])/fees[2])*fees[3])
    return answer
