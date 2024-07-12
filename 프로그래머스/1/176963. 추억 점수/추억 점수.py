def solution(name, yearning, photo):
    answer = []
    
    for i in photo:
        count = 0
        for j in range(len(name)):
            if name[j] in i:
                count += yearning[j]
        answer.append(count)
    return answer