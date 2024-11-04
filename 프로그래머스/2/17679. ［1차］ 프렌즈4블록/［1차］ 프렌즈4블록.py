def solution(m, n, board):
    answer = 0
    board = [list(i) for i in board]
    
    block = set()
    while True:
        for i in range(m-1):
            for j in range(n-1):
                b = board[i][j]
                if b == []:
                    continue
                else:
                    if board[i+1][j] == b and board[i][j+1] == b and board[i+1][j+1] == b:
                        block.add((i,j))
                        block.add((i+1,j))
                        block.add((i,j+1))
                        block.add((i+1,j+1))
                           
        if block:
            answer += len(block)
            for i, j in block:
                board[i][j] = []
            block = set()
        else:
            break
            
        while True:
            r = 0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and board[i+1][j] == []:
                        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                        r = 1
                        
            if r == 0:
                break
                    
    return answer

# # 실패
# def solution(m, n, board):
#     answer = 0
    
#     # 오른쪽, 아래, 대각선 아래 
#     dx = [0,0,1,1]
#     dy = [0,1,0,1]
    
#     lst = []
#     for b in board:
#         lst.append(list(b))
        
#     while True:
#         a = 0
#         for i in range(m-1):
#             for j in range(n-1):
#                 block = board[i][j]
#                 if block != []:
#                     cnt = 0
#                     for k in range(len(dx)):
#                         x = i + dx[k]
#                         y = j + dy[k]

#                         if block == board[x][y]:
#                             cnt += 1

#                     if cnt == 4:
#                         for k in range(len(dx)):
#                             lst[i+dx[k]][j+dy[k]] = []  
#                             a = 1
#                 else:
#                     continue
                        
#         if a == 0:
#             break
        
#         board = lst
        
#         while True:
#             r = 0
#             for i in range(m-1):
#                 for j in range(n):
#                     if board[i][j] and board[i+1][j] == []:
#                         board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
#                         r = 1
#             if r == 0:
#                 break

#     for i in range(m):
#         answer += board[i].count([])

#     return answer