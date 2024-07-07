def solution(n, m):
    answer = []
    
    lst = []
    
    for i in range(1,min(n,m)+1):
        if (n%i == 0) and (m%i == 0):
            lst.append(i)
    
    gcf = max(lst) # 최대 공약수

    lcm = gcf * (n/gcf) * (m/gcf) # 최소 공배수

    answer.append(gcf)
    answer.append(lcm)
    return answer