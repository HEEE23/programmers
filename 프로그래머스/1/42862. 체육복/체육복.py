def solution(n, lost, reserve):
    answer = n - len(lost)
    
    lst = []
    lost.sort()
    for l in lost:
        if l in reserve:
            answer += 1
            reserve.remove(l)
        else:
            if l-1 in reserve:
                answer += 1
                reserve.remove(l-1)
                continue
            elif l+1 in reserve:
                if l+1 in lost:
                    continue
                answer += 1
                reserve.remove(l+1)
                continue

            

    return answer