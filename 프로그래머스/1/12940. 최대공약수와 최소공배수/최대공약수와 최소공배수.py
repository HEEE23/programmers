def solution(n, m):
    lst = []
    for i in range(1,min(n,m)+1):
        if (n%i == 0) and (m%i == 0):
            lst.append(i)
    
    gcd = max(lst) # 최대 공약수

    lcm = gcd * (n/gcd) * (m/gcd) # 최소 공배수

    answer = [gcd, lcm]
    return answer