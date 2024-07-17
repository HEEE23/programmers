def solution(n, m, section):
    answer = 0
    
    lst = [1]*n
    for i in section:
        lst[i-1] = 0
    
    paint = [1]*m
    # for i in range(section[0]-1, n-m+1):
    #     if 0 not in lst:
    #         break
    #     else:
    #         if 0 in lst[i:i+m]: 
    #             lst[i:i+m] = paint
    #             answer += 1
    
    for i in range(len(lst)):
        if lst[i] == 0:
            lst[i:i+m] = paint
            answer += 1
            
    return answer