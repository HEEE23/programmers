def solution(array, commands):
    answer = []
    result = []
    for i in commands:
        result = array[i[0]-1:i[1]]
        result.sort()
        answer.append(result[i[2]-1])
        
    return answer