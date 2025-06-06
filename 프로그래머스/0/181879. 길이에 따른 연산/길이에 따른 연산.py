def solution(num_list):
    answer = 0
    
    if len(num_list) >= 11:
        answer = sum(num_list)
    else:
        s = 1
        for n in num_list:
            s *= n
        answer = s
        
    return answer