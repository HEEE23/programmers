from collections import deque
def solution(n, wires):
    answer = -1
    
    lst = []
    a, b = 0, 0
    for i in range(len(wires)):
        wirea = wires[i]
        wireb = wires[:i] + wires[i+1:]
        
        graph = [[] for _ in range(n+1)]
        for w in wireb:
            graph[w[0]].append(w[1])
            graph[w[1]].append(w[0])

        visited = [0 for _ in range(n+1)]
        queue = deque()
        queue.append(1)  
        visited[1] = 1
        count = 1

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = 1
                    queue.append(neighbor)
                    count += 1

        # 두 송전망 크기 차이 계산
        lst.append(abs((n - count) - count))
    answer = min(lst)
    return answer