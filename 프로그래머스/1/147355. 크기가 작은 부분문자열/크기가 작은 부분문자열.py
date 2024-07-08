def solution(t, p):
    answer = 0
    lst = []
    for i in range(len(t)-len(p)+1):
        lst.append(t[i:i+len(p)])
        
    count = 0
    for i in range(len(lst)):
        if lst[i] <= p:
            count += 1
    answer = count
    return answer