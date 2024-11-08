def solution(n):                                                        
    answer = ''
    
    country = [4, 1, 2]
    lst = []
    
    q = 1
    while q != 0:
        q = n // 3
        r = n % 3
        if r == 0:
            q -= 1
        lst.append(country[r])
        n -= 1
        n = n // 3

    lst = lst[::-1]

    answer = ''.join(map(str,lst))
    return answer