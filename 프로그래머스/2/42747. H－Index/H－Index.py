def solution(citations):
    answer = 0
    
    citations.sort()

    h = []

    n = len(citations)
    while n != 1:
        lst_u = []
        lst_l = []

        for c in citations:
            if c >= n:
                lst_u.append(c)
            else:
                lst_l.append(c)
                
        # i번 이상 인용된 논문이 i편 이상이고 나머지 논문이 h번 이하 인용되었다면,
        if n <= len(lst_u) and n >= len(lst_l):
            answer = n
            break
        n -= 1
    return answer