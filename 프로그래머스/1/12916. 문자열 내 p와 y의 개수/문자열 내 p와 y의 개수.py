def solution(s):
    answer = True
    
    s1 = s.lower()
    p_count = 0
    y_count = 0
    for i in s1:
        if i == 'p':
            p_count += 1
        elif i == 'y':
            y_count += 1

    if p_count == y_count:
        return True
    else:
        return False
    return True