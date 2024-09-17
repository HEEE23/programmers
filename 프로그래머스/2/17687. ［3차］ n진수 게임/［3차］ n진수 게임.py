def solution(n, t, m, p):
    answer = ''
    
    lst = ['0', '1']

    for i in range(2, t*m):
        if len(lst) < t*m:
            s = ''

            n1 = n
            while i > 0:
                i, mod = divmod(i, n1)
                if mod == 10:
                    s += 'A'
                elif mod == 11:
                    s += 'B'
                elif mod == 12:
                    s += 'C'
                elif mod == 13:
                    s += 'D'
                elif mod == 14:
                    s += 'E'
                elif mod == 15:
                    s += 'F'
                else:
                    s += str(mod)

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