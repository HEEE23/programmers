from collections import deque

def bfs(start, end, maps):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    q = deque()

    # 초깃값 설정
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == start:    
                q.append((i, j, 0))    
                visited[i][j] = True
                break

    while q:
        x, y, answer = q.popleft()
        
        if maps[x][y] == end:
            return answer
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 'X':
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny, answer + 1))
    return -1
                    
def solution(maps):
    path1 = bfs('S','L', maps)
    path2 = bfs('L','E', maps)
    
    if path1 != -1 and path2 != -1:
        return path1 + path2
                    
    return -1