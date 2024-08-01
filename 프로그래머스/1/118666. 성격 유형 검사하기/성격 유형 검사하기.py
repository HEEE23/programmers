def solution(survey, choices):
    answer = '' 
    personality = {'R': 0, 'T' : 0, 'C': 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    
    for i in range(len(choices)):
        if choices[i] < 4:
            personality[survey[i][0]] += (4-choices[i])
        elif choices[i] > 4:
            personality[survey[i][1]] += (choices[i]-4)
    
    if max(personality['R'], personality['T']) == personality['R']:
        answer += 'R'
    else:
        answer += 'T'
        
    if max(personality['C'], personality['F']) == personality['C']:
        answer += 'C'
    else:
        answer += 'F'
        
    if max(personality['J'], personality['M']) == personality['J']:
        answer += 'J'
    else:
        answer += 'M'
        
    if max(personality['A'], personality['N']) == personality['A']:
        answer += 'A'
    else:
        answer += 'N'

    return answer