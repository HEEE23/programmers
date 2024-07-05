def solution(n):
    answer = 0

    lst = []
    for i in range(1,n+1):
        if ( (i == n/i) and (n%i == 0)):
            lst.append(i)
            break
            
    if len(lst) == 0:
        answer = -1
    else:
        answer = (lst[0]+1)**2
        
    return answer

    