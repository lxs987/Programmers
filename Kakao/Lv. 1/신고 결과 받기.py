# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    # 각 인원이 신고를 당한 횟수를 저장할 리스트 report_n
    report_n = [0 for _ in range(len(id_list))]
    # 중복 제거
    report_set = set(report)
    report_list = list(report_set)
    for i in range(len(report_list)):
        r1 = report_list[i].split()
        report_n[id_list.index(r1[1])] += 1
        # report_n 실행 결과: 신고된 횟수:  [1, 2, 0, 2]
        
    for i in range(len(report_list)):
        r1 = report_list[i].split()
        # 만약 신고한 사용자의 신고된 횟수가 2를 초과한다면, 신고자에게 +1 (처리메일발송횟수)
        if report_n[id_list.index(r1[1])] > k-1:
            answer[id_list.index(r1[0])] += 1
    return answer