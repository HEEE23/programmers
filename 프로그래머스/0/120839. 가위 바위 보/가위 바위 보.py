def solution(rsp):
    answer = ''
    
    rsp = list(rsp)
    
    for r in rsp:
        if r == '2':
            answer += '0'
        elif r == '0':
            answer += '5'
        elif r == '5':
            answer += '2'
    
    return answer