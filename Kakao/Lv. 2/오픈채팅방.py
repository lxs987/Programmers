# -*- coding: utf-8 -*-
"""
Created on Fri May 27 18:42:19 2022

@author: Jinkyung
"""

def solution(record):
    answer = []
    userDB = dict()
    actions = []
    
    for event in record:
        info = event.split()
        action, userid = info[0], info[1]
        if action in ("Enter", "Change"):
            nickname = info[2]
            # 딕셔너리에 저장
            userDB[userid] = nickname
        actions.append((action, userid))
        
    for actionInfo in actions:
        action, userid = actionInfo[0], actionInfo[1]
        if action == 'Enter':
            answer.append(f'{userDB[userid]}님이 들어왔습니다.');
        elif action == 'Leave':
            answer.append(f'{userDB[userid]}님이 나갔습니다.');
    return answer

# 참고한 사이트: https://latte-is-horse.tistory.com/131
