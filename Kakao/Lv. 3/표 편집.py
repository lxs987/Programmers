def solution(n, k, cmd):
    deleted = []
    sheet = []
    for i in range(n):
        sheet.append([i - 1, i + 1])
    for c in cmd:
        order = c.split(' ')
        # 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
        if order[0] == 'U':
            for _ in range(int(order[1])):
                k = sheet[k][0]
        # 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
        elif order[0] == 'D':
            for _ in range(int(order[1])):
                k = sheet[k][1]
        # 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
        elif order[0] == 'C':
            deleted.append((k, sheet[k]))
            if not sheet[k][0] == -1:
                sheet[sheet[k][0]][1] = sheet[k][1]
            if not sheet[k][1] == n:
                sheet[sheet[k][1]][0] = sheet[k][0]
            if sheet[k][1] == n:
                k = sheet[k][0]
            else:
                k = sheet[k][1]
        # 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.
        elif order[0] == 'Z':
            lastDeleted = deleted.pop()
            if not lastDeleted[1][0] == -1:
                sheet[lastDeleted[1][0]][1] = lastDeleted[0]
            if not lastDeleted[1][1] == n:
                sheet[lastDeleted[1][1]][0] = lastDeleted[0]

    answer = ['O'] * n
    for d in deleted:
        answer[d[0]] = 'X'
    return ''.join(answer)
