def solution(board, moves):
    answer = 0
    board_t = list(map(list, zip(*board)))
    
    doll = []
    for m in moves:
        lst = []
        for i in range(len(board_t[m-1])):
            if board_t[m-1][i] != 0:
                lst.append(board_t[m-1][i])
                board_t[m-1][i] = 0
                break
        if len(lst) == 0:
            continue
        else:
            doll.append(lst[0])
            if len(doll) >= 2:
                if doll[-2] == doll[-1]:
                    del doll[-2:]
                    answer += 2 
    
    return answer