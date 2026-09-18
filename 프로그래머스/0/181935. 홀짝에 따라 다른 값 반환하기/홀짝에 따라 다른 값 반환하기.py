def solution(n):
    answer = 0
    
    if n%2:
        return sum(range(1, n+1, 2))
    else:
        return sum([i*i for i in range(2, n+1, 2)])
    
    # if n % 2 == 0:
    #     for i in range(1, n+1):
    #         if i % 2 == 0:
    #             answer += i**2
    # else:
    #     for i in range(1, n+1):
    #         if i % 2 != 0:
    #             answer += i
                
    return answer