def solution(n, s, a, b, fares):
    answer = 1e10
    
    graph = [[1e10]*(n+1) for _ in range(n+1)]
    
    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                graph[i][j] = 0
                
    for fare in fares:
        c, d, f = fare
        graph[c][d] = f
        graph[d][c] = f

    # 플로이드 와샬
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    for i in range(1,n+1):
        tmp = graph[s][i] + graph[i][a] + graph[i][b]
        answer = min(tmp, answer)
    return answer