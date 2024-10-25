def solution(record):
    answer = []
    
    dic = {}
    for r in record:
        if ('Enter' in r) or ('Change' in r):
            state, uid, nickname = r.split()
            dic[uid] = nickname

    for r in record:
        if 'Enter' == r.split()[0]:
            answer.append(f'{dic[r.split()[1]]}님이 들어왔습니다.')
        elif 'Leave' == r.split()[0]:
            answer.append(f'{dic[r.split()[1]]}님이 나갔습니다.')
    return answer