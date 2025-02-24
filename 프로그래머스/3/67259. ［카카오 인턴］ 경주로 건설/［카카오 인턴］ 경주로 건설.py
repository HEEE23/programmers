from collections import deque
def solution(board):
    def bfs(start):
        direc = {0 : [-1,0], 1 : [0,1], 2 : [1,0], 3 : [0,-1]} # 북, 동, 남, 서
        
        n = len(board)
        dp = [[int(1e9)]*n for _ in range(n)]
        dp[0][0] = 0
        
        q = deque([start])
        while q:
            x, y, cost, d = q.popleft()
            for i in range(4):
                nx = x + direc[i][0]
                ny = y + direc[i][1]
                
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                    # 직선인 경우
                    if i == d: 
                        ncost = cost + 100
                    # 코너인 경우(직선도로 100 + 코너 500)
                    else:
                        ncost = cost + 600
                        
                    if ncost < dp[nx][ny]:
                        dp[nx][ny] = ncost
                        q.append([nx, ny, ncost, i])
        return dp[-1][-1]
    
    return min(bfs((0,0,0,1)), bfs((0,0,0,2))) # 오른쪽 방향으로 시작, 아래 방향으로 시작

# # 25번 오답. 무조건 최솟값인 경우에 도로를 건설하면 정답이 최소가 아닐 수 있음
# from collections import deque
# def solution(board):
#     answer = int(1e9)
#     n = len(board)
    
#     q = deque()
    
#     q.append(((0,0),0, [(0,0)]))
    
#     # 상, 하, 좌, 우
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]
    
#     dp = [[int(1e9)]*n for _ in range(n)]
#     dp[0][0] = 0
    
#     while q:
#         where, price, visited = q.popleft()
#         x, y = where
        
#         if price > dp[x][y]:
#             continue
#         else:
#             dp[x][y] = price
        
#         if x == n-1 and y == n-1:
#             answer = min(answer, price)
#             continue
            
#         if answer <= price:
#             continue
            
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#             if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and not (nx, ny) in visited:
#                 if x == 0 and y == 0:
#                     q.append(((nx, ny), 100 + price, visited + [(nx, ny)]))
#                 else:
#                     # 직선(가로 or 세로)일 경우
#                     if (visited[-2][0] == nx == visited[-1][0]) or (visited[-1][1] == ny == visited[-2][1]):
#                         q.append(((nx,ny), 100 + price, visited + [(nx, ny)]))
#                     # 코너(직선 도로 100 + 코너 500)인경우
#                     else:
#                         q.append(((nx, ny), 600 + price, visited + [(nx, ny)]))
#     return answer