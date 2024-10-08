def solution(n):
    answer = 0
    
    f = [0]*(n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = (f[i-1] + f[i-2])%1234567
    
    answer = f[n] 
    return answer