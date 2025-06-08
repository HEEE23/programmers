def solution(myString):
    answer = ''
    myString = list(myString)
    
    for i in range(len(myString)):
        if ord(myString[i]) < 108:
            myString[i] = 'l'
            
    answer = ''.join(myString)
    return answer