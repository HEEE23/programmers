def solution(n, control):
    control = list(control)
    
    for c in control:
        if c == 'w':
            n += 1
        elif c == 's':
            n -= 1
        elif c == 'd':
            n += 10
        else:
            n -= 10
    
    answer = n
    
    return answer