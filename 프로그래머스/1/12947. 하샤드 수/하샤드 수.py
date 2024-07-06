def solution(x):
    answer = True
    lst = list(map(int,str(x)))
    lst_sum = sum(lst)
    
    if x%lst_sum != 0:
        answer = False
    
    return answer