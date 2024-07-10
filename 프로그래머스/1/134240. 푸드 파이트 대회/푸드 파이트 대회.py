def solution(food):
    answer = ''
    count = 0
    for i in range(1,len(food)):
        if food[i] >= 2:
            count = int(food[i]/2)
            for j in range(count):
                answer += str(i)
    answer += '0'
    for i in range(len(answer)-2,-1,-1):
        answer += answer[i]
    return answer