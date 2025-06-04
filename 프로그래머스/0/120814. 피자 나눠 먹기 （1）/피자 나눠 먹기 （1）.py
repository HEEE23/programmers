def solution(n):
    answer = 0
    
    print(n//7)
    if n <= 7:
        answer = 1
    else:
        if n % 7 == 0:
            answer = (n//7)
        else:
            answer = (n//7)+1
    return answer