def solution(lottos, win_nums):
    answer = []
    
    count = 0
    for l in lottos:
        if l in win_nums:
            count += 1
    
    doddle = lottos.count(0)
    
    h_rank = count+doddle
    l_rank = count
    
    for rank in (h_rank, l_rank):
        if rank == 6:
            answer.append(1)
        elif rank == 5:
            answer.append(2)
        elif rank == 4:
            answer.append(3)
        elif rank == 3:
            answer.append(4)
        elif rank == 2:
            answer.append(5)
        else:
            answer.append(6)
    return answer