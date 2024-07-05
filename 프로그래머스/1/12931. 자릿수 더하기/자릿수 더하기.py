def solution(n):
    answer = 0
    
    lst = map(int, str(n))
    for i in lst:
        answer += i

    return answer