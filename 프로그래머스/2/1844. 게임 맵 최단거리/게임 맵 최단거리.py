# from collections import deque
# def solution(maps):
#     n = len(maps)
#     m = len(maps[0])
    
#     visited = [[0]*m for _ in range(n)]
    
#     queue = deque()
#     queue.append((0,0))
#     visited[0][0] = 1
    
#     dx = [-1,1,0,0]
#     dy = [0,0,1,1]
#     while queue:
#         x, y = queue.popleft()
        
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#             if 0 <= nx < n and 0 <= ny < m:
#                 if visited[nx][ny] == 0 and maps[nx][ny] == 1:
#                     visited[nx][ny] = 1
#                     maps[nx][ny] = maps[x][y] + 1
#                     queue.append((nx,ny))
                    
#     if maps[n-1][m-1] == 1:
#         return -1
#     else:
#         return maps[n-1][m-1]

from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[0]*m for i in range(n)]
    
    queue = deque()
    queue.append((0,0))
    visited[0][0] = 1
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx,ny))
                    visited[nx][ny] = 1

    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]
    return