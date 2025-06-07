from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    
    graph = [[] for _ in range(n+1)]
    
    for r in roads:
        graph[r[0]].append(r[1])
        graph[r[1]].append(r[0])

    visited = [-1]*(n+1)
    
    # 거꾸러 생각해야됨, destination에서 출발
    q = deque([destination])
    visited[destination] = 0
    while q:
        now = q.popleft()
        
        for n in graph[now]:
            if visited[n] == -1:
                visited[n] = visited[now] + 1
                q.append(n)
    
    answer = [visited[i] for i in sources]
    return answer

# from collections import deque
# def solution(n, roads, sources, destination):
#     answer = []
    
#     graph = [[] for _ in range(n+1)]
    
#     for r in roads:
#         graph[r[0]].append(r[1])
#         graph[r[1]].append(r[0])
    
#     for s in sources:
#         print(s)
#         queue = deque()
         
#         # 강철부대지역일 경우
#         if s == destination:
#             answer.append(0)
#             break
            
#         if len(graph[s]) == 0:
#             answer.append(-1)
#             break
            
#         step = 1
#         for e in graph[s]:
#             queue.append((s, e, step))
            
#         visited = [0 for _ in range(n+1)]
#         visited[s] = 1
        
#         while queue:
#             for i in range(len(queue)):
#                 start, end, step = queue.popleft()
                
#                 if end == destination:
#                     answer.append(step)
#                     break
                    
#                 if not visited[end]:
#                     visited[end] = 1
#                     step += 1
#                     for a in graph[end]:
#                         queue.append((end, a, step))
            
#             if end == destination:
#                 break

#     return answer