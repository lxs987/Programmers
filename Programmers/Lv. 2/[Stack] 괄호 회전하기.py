# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a posorary script file.
"""

dic = {"]": "[", ")": "(", "}": "{"}


def solution(s):
    answer = 0

    cnt = 0
    # s의 길이동안 while문 실행
    while cnt != len(s):
        stack = []
        # while문 한 턴 돌 때마다 s를 회전시킴
        s = s[1:len(s)] + s[0]
        answer_s = True

        # 시작하는 괄호라면 stack에 추가함
        for c in s:
            if c == "[" or c == "(" or c == "{":
                stack.append(c)
            # 마치는 괄호일 때
            else:
                # 이전에 여는 괄호가 나오지 않았으므로 false
                if len(stack) == 0:
                    answer_s = False
                    break
                # 여는 괄호가 stack에 존재하고 있으면 pop (올바른 괄호)
                if dic[c] == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    answer_s = False
                    break

        # pop 되지 않고 남아있는 괄호가 있다면 false
        if len(stack) != 0:
            answer_s = False

        # true라면 올바른 괄호의 갯수에 +1
        if answer_s == True:
            answer += 1

        cnt += 1

    return answer

# 시간복잡도 좋지 않음
# def solution(s):
#     answer = 0
#     pos = list(s)

#     for _ in range(len(s)):

#         stack = []
#         for i in range(len(pos)):
#             if len(stack) > 0:
#                 if stack[-1] == '[' and pos[i] == ']':
#                     stack.pop()
#                 elif stack[-1] == '(' and pos[i] == ')':
#                     stack.pop()
#                 elif stack[-1] == '{' and pos[i] == '}':
#                     stack.pop()
#                 else:
#                     stack.append(pos[i])
#             else:
#                 stack.append(pos[i])
#         if len(stack) == 0:
#             answer += 1
#         pos.append(pos.pop(0))

#     return answer
