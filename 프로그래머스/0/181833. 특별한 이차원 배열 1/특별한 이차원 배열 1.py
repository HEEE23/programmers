def solution(n):
    answer = []
    
    for i in range(n):
        lst = []
        for j in range(n):
            if i == j:
                lst.append(1)
            else:
                lst.append(0)
                
        answer.append(lst)
        
    return answer