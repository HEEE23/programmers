import math
def solution(n, k):
    answer = []

    lst = [i for i in range(1, n+1)]
    
    while lst:
        a = (k-1) // math.factorial(n-1)
        answer.append(lst.pop(a))
        k %= math.factorial(n-1)
        n -= 1
        
    # # 시간초과
    # lst = [i for i in range(1,n+1)]
    # line = list(permutations(lst))
    # answer = list(line[k-1])
    
    return answer