def solution(a, b):
    answer = 0
    
    a, b = str(a), str(b)
    
    answer = max(int(a+b), int(b+a))
    return answer