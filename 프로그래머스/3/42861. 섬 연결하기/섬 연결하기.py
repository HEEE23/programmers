import heapq
def solution(n, costs):
    answer = 0
    
    graph = [[] for _ in range(n)]
    visited = [False]*len(graph)
    
    # 연결된 노드끼리 리스트 변환 
    for c in costs:
        graph[c[0]].append((c[1],c[2]))
        graph[c[1]].append((c[0],c[2]))
    
    # 시작 노드
    start = 0
    visited[start] = True
    
    # 시작 노드와 연결된 간선 추가 
    heap = []
    for end, cost in graph[start]:
        heapq.heappush(heap, (cost, start, end))
    
    while heap:
        # 최소 비용인 간선 pop
        cost, start, end = heapq.heappop(heap)
        
        # 이미 방문한 경우 다음 간선, 중복 처리
        if visited[end]:
            continue
            
        # 끝점 노드 방문 처리
        visited[end] = True
        answer += cost
        
        # 끝점 노드와 연결된 간선 추가
        for next_end, next_cost in graph[end]:
            heapq.heappush(heap, (next_cost, end, next_end))
        
    return answer