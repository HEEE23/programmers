def solution(board, skill):
    answer = 0
    
    # 누적합 이용
    prefix = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    for s in skill:
        t, r1, c1, r2, c2, degree = s
        if t == 1:
            prefix[r1][c1] -= degree
            prefix[r2+1][c2+1] -= degree
            prefix[r1][c2+1] += degree
            prefix[r2+1][c1] += degree
        else:
            prefix[r1][c1] += degree
            prefix[r2+1][c2+1] += degree
            prefix[r1][c2+1] -= degree
            prefix[r2+1][c1] -= degree
    
    # 아래로 누적합
    for j in range(len(prefix[0])):
        a = 0
        for i in range(len(prefix)):
            a += prefix[i][j]
            prefix[i][j] = a
    
    # 왼쪽에서 오른쪽으로 누적합
    for i in range(len(prefix)):
        a = 0
        for j in range(len(prefix[0])):
            a += prefix[i][j]
            prefix[i][j] = a

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += prefix[i][j]
            if board[i][j] > 0:
                answer += 1

#     # 시간 초과
#     for s in skill:
#         t, r1, c1, r2, c2, degree = s
        
#         for i in range(r1, r2+1):
#             for j in range(c1, c2+1):
#                 if t == 1:
#                     board[i][j] -= degree
#                 else:
#                     board[i][j] += degree
    
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             if board[i][j] > 0:
#                 answer += 1
    return answer