def solution(n, results):
    answer = 0
    
    graph = [[0]*n for _ in range(n)]
    
    # 이기면 1, 지면 -1
    for a, b in results:
        graph[a-1][b-1] = 1
        graph[b-1][a-1] = -1
        
    # 플로이드 - 와샬 알고리즘
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
    
    # 0이 하나인 경우 = 정확하게 순위를 매길 수 있는 선수의 수
    for g in graph:
        if g.count(0) == 1:
            answer += 1
            
    return answer