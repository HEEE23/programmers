def solution(k, score):
    answer = []
    
    hof = []
    for i in range(len(score)):
        hof.append(score[i])
        hof.sort()
        if len(hof) > k:
            hof = hof[len(hof)-k:len(hof)+1]
        answer.append(hof[0])
    return answer