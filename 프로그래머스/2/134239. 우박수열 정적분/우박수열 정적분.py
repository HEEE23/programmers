def solution(k, ranges):
    answer = []
    
    # collatz
    n = 0
    lst = []
    while k != 1:
        lst.append(int(k))
        if k % 2 == 0:
            k /= 2
        else:
            k = 3*k+1
        n += 1
    lst.append(1)

    area = []
    for i in range(len(lst)-1):
        area.append((lst[i]+lst[i+1])/2)
        
    for r in ranges:
        a, b = r[0], n+r[1]
        if a > b:
            answer.append(-1)
        else:
            answer.append(sum(area[a:b]))

    return answer