def solution(n):                                                        
    answer = ''
    
    country = ['4', '1', '2']
    
    lst = [] 
    while n != 0:
        r = n % 3
        n = n // 3
        if r == 0:
            n -= 1
        lst.append(country[r])

    lst = lst[::-1]

    answer = ''.join(lst)
    return answer