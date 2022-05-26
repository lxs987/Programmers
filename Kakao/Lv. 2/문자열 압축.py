def solution(s):
    # 쪼갠 문자열의 길이들을 담는 list
    result = []
    if len(s)==1:
        return 1
    # 쪼갤 수 있는 최대 길이: 문자열 s의 1/2
    for i in range(1, (len(s)//2)+1):
        # 매번 쪼갰을 때 나오는 문자열 저장
        b = ''
        cnt = 1
        tmp = s[:i]
        
        for j in range(i, len(s), i):
            if tmp == s[j:i+j]:
                cnt += 1
            else:
                if cnt!=1:
                    b = b + str(cnt) + tmp
                else:
                    b = b + tmp
                tmp = s[j:j+i]
                cnt = 1
            
        if cnt != 1:
            b = b + str(cnt) + tmp
        else:
            b = b + tmp
        
        result.append(len(b))
    return min(result)
# 참고:  https://eunhee-programming.tistory.com/135