def solution(answers):
    answer = []
    
    person_1 = [1,2,3,4,5]
    person_2 = [2,1,2,3,2,4,2,5]
    person_3 = [3,3,1,1,2,2,4,4,5,5]
    
    result = []
    for person in (person_1, person_2, person_3):
        count = 0         
        for i in range(len(answers)):
            if answers[i] == person[i%len(person)]:
                count += 1          

        result.append(count)
    
    answer = list(filter(lambda x : result[x] == max(result), range(len(result))))
    
    for i in range(len(answer)):
        answer[i] = answer[i] + 1

    return answer