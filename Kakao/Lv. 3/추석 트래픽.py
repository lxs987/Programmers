# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 15:12:38 2022

@author: Jinkyung
"""

def solution(lines):
    answer = 0
    log = []

    for line in lines:
        date, s, t = line.split()  # 날짜(사용X), 응답완료시간, 처리시간
        s = s.split(':')
        t = t.replace('s', '')

        end = (int(s[0])*3600 + int(s[1])*60 + float(s[2])) * \
            1000  # 끝시간을 msec 단위로 저장
        start = end - float(t)*1000 + 1  # 시작 시간을 msec 단위로 저장
        log.append([start, end])

    for start, end in log:
        # 최대 초당 처리량 구하기
        answer = max(answer, throughput(log, start, start + 1000),
                     throughput(log, end, end + 1000))

    return answer

# 초당 처리량을 구하는 함수
def throughput(log, start, end):
    cnt = 0
    for x in log:
        if x[0] < end and x[1] >= start:
            cnt += 1
    return cnt
