def solution(myString, pat):
    answer = 0
    
    myString = list(myString)
    for i in range(len(myString)):
        if myString[i] == 'A':
            myString[i] = 'B'
        else:
            myString[i] = 'A'
    
    myString = ''.join(myString)
    
    if pat in myString:
        answer = 1
        
    return answer