def solution(files):
    answer = []
    
    lst = []
    # HEAD, NUMBER, TAIL 분리
    for f in files:
        head, number, tail = '', '', ''
        for i in range(len(f)):
            if f[i].isdigit():
                number += f[i]
            elif not number:
                head += f[i]
            else:
                tail += f[i:]
                break
        lst.append((head,number,tail))
    
    # 1. HEAD 사전순으로 정렬, 2. NUMBER의 숫자순, 3. 원래 입력에 주어진 순서
    lst.sort(key = lambda x : (x[0].lower(), int(x[1])))
    
    for l in lst:
        answer.append(''.join(l))
    return answer
