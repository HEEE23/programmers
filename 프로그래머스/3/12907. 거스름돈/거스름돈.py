def solution(n, money):
    answer = 0
    
    dp = [0] * (n + 1)
    
    # 0원 : 아무것도 선택하지 않을 경우
    dp[0] = 1
    
    # i원을 만들 수 있는 경우의 수
    for m in money:
        for i in range(m, n+1):
            dp[i] += dp[i-m]
            
    answer = dp[n] % 1000000007
    return answer