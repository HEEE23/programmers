def solution(n, s):
    answer = []
    
    while n != 0:
        a = int(s/n)
        if a == 0:
            return [-1]
        answer.append(a)
        s -= a
        n -= 1
        
        
    return answer