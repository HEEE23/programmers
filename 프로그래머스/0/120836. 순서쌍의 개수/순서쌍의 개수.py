def solution(n):
    answer = 0
    
    lst = []
    for i in range(1, n+1):
        if n%i == 0:
            lst.append(i)
            
    answer = len(lst)
    return answer