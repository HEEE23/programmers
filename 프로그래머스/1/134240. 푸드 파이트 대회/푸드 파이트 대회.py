def solution(food):
    answer = ''
    count = 0
    for i in range(1,len(food)):
        if food[i] >= 2:
            count = int(food[i]/2)
            for j in range(count):
                answer += str(i)
    answer_r = answer[::-1]
    answer += '0'
    answer += answer_r
    return answer