def solution(m, n, puddles):
    answer = 0
    
    puddles = [[q,p] for [p,q] in puddles]
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    # 집이 있는 곳
    dp[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1: 
                continue

            # 물에 잠긴 지역
            if [i,j] in puddles:
                dp[i][j] = 0
            else:
                # 왼쪽 칸과 위 칸에서 올 수 있는 경로의 개수 합산
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) %1000000007
    
    answer = dp[n][m]
    return answer