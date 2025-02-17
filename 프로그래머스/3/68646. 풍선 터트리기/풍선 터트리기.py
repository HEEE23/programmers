def solution(a):
    # 양 끝 값은 늘 최후까지 남을 수 있음
    answer = 2
    
    dp = [[0 for _ in range(len(a))] for _ in range(2)]
    
    dp[0][0] = a[0]
    dp[1][-1] = a[-1]
    
    # 왼쪽 -> 오른쪽 최솟값
    for i in range(1,len(a)):
        dp[0][i] = min(dp[0][i-1], a[i])
    
    # 오른쪽 -> 왼쪽 최솟값
    for i in range(len(a)-2,-1,-1):
        dp[1][i] = min(dp[1][i+1], a[i])
        
    for i in range(1,len(a)-1):
        left_min = dp[0][i-1]
        right_min = dp[1][i+1]
        
        # 왼쪽 최솟값, 오른쪽 최솟값보다 클 경우; 가장 작은값
        if left_min > a[i] and right_min > a[i]:
            answer += 1
        # 왼쪽 최솟값보다 작고 오른쪽 최솟값보다 클 경우, 왼쪽 최솟값보다 크고 오른쪽 최솟값보다 작을 경우
        elif (left_min > a[i] and right_min < a[i]) or (left_min < a[i] and right_min > a[i]):
            answer += 1
    return answer