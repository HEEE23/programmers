def solution(board, h, w):
    answer = 0
    
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    n = len(board)
    color = board[h][w]
    for i in range(len(dh)):
        h_check = h + dh[i]
        w_check = w + dw[i]
        
        if h_check >= 0 and h_check < n:
            if w_check >= 0 and w_check < n:
                if color == board[h_check][w_check]:
                    answer += 1
            
    return answer