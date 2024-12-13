def solution(maps):
    answer = []
    
    n, m = len(maps[0]), len(maps)
    visited = [[0]*n for _ in range(m)]
    
    # 상,하,좌,우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    for i in range(m):
        for j in range(n):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                period = 0
                q = [(i,j)]
                
                while q:
                    x, y = q.pop()
                    if visited[x][y]:
                        continue
                    
                    visited[x][y] = 1
                    period += int(maps[x][y])
                    
                    for k in range(4):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] != 'X' and visited[nx][ny] == 0:
                            q.append((nx,ny))
            
                answer.append(period)
    if answer:
        answer.sort()
    else:
        answer.append(-1)
    return answer