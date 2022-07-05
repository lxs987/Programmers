# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 16:26:58 2022

@author: Jinkyung
"""

def solution(n, t, m, timetable):
    crewArrive = [int(time[:2])*60 + int(time[3:]) for time in timetable]
    crewArrive.sort()

    busTime = [9*60 + t*i for i in range(n)]

    index = 0
    for bus in busTime:
        cnt = 0
        # 버스에 오른 인원이 인원제한(m)보다 적고,
        # 버스에 오른 크루의 순서가 총 크루의 인원보다 작으면서,
        # 현재 버스 시간보다 현재 크루가 도착한 시간이 먼저거나 같을 경우
        # 버스에 오른 인원 + 1, 탑승 순서 +1
        while cnt < m and index < len(crewArrive) and crewArrive[index] <= bus:
            index += 1
            cnt += 1
        # 버스에 자리가 남았을 경우, 버스 출발시간 return
        if cnt < m:
            answer = bus
        # 버스에 자리가 없는 경우, 맨 마지막 크루보다 1분 먼저 도착
        else:
            answer = crewArrive[index - 1] - 1

    return str(answer//60).zfill(2) + ":" + str(answer % 60).zfill(2)
