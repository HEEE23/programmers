def solution(n, t, m, p):
    answer = ''
    
    lst = ['0', '1']

    for i in range(2, t*m):
        if len(lst) < t*m:
            s = ''

            NUMBERS = '0123456789ABCDEF'
            n1 = n
            while i > 0:
                i, mod = divmod(i, n1)
                s += NUMBERS[mod]

            s = s[::-1]
            lst.extend(list(s))
        else:
            break
    
    for i in range(p-1, len(lst), m):
        if len(answer) == t:
            break
        else:
            answer += lst[i]
    return answer