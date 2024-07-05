def solution(n):
    answer = 0
    lst = list(str(n))
    lst.sort(reverse=True)
    
    answer = int(''.join(lst))
    return answer