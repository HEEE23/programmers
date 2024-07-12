def solution(name, yearning, photo):
    answer = []
    m = list(zip(name, yearning))
    
    for i in photo:
        count = 0
        for j in range(len(name)):
            if name[j] in i:
                count += yearning[j]
            else:
                count += 0
        answer.append(count)
    return answer