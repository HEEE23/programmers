def solution(array, commands):
    answer = []
    
    for c in commands:
        result = sorted(array[c[0]-1:c[1]])
        answer.append(result[(c[2]-1)%len(result)])
        
        
    # result = []
    # for i in commands:
    #     result = array[i[0]-1:i[1]]
    #     result.sort()
    #     answer.append(result[i[2]-1])
        
    return answer