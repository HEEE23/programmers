def solution(n):
    answer = 0
    
    d = [0]*(n+1)
    
    d[0] = 1
    d[2] = 3
    for i in range(4,n+1):
        if i%2==0:
            d[i] = (4*d[i-2]-d[i-4])%1000000007
        else:
            d[i] = 0

    answer = d[n]
    return answer