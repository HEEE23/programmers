def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    visited = [False]*len(graph)

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    # 1번 노드까지 간선의 개수
    cnt = [0]*(n+1)
    a = 1
    
    # 1번 노드 방문 처리
    start = 1
    visited[start] = True
    
    # 1번 노드와 연결된 노드 추가
    q = []
    for s in graph[start]:
        q.append((start,s))

    while q:
        for i in range(len(q)):
            start, end = q.pop(0)
            
            if visited[end]:
                continue
                
            cnt[end] = a  
            visited[end] = True
            
            for e in graph[end]:
                q.append((end, e))    
        a += 1
    
    max_edge = max(cnt)
    answer = cnt.count(max_edge)
    
    return answer