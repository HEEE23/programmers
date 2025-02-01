def solution(operations):
    answer = []
    
    q = []
    for o in operations:
        cmd, num = o.split(' ')
        num = int(num)

        if cmd == 'I':
            q.append(num)
        else:
            if num == 1:
                if q:
                    q.pop(q.index(max(q)))
            else:
                if q:
                    q.pop(q.index(min(q)))
    
    if q:
        answer.extend([max(q),min(q)])
    else:
        return [0,0]
    
    return answer