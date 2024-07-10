def solution(numbers):
    answer = []

    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
            
    #answer = sorted(list(set(answer)))
    lst = []
    for result in answer:
        if result not in lst:
            lst.append(result)            
    lst.sort()
    answer = lst
    return answer