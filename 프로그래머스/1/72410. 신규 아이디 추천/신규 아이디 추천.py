def solution(new_id):
    answer = ''
    
    answer = new_id.lower()
    
    cha = ['`','~','!','@','#','$','%','^','&','*','(',')','=',';',':',',','"','<','>','/','?','+','[',']','{','}','\\']
           
    for c in cha:
        answer = answer.replace(c, '')
        
    while '..' in answer:
        answer = answer.replace('..','.')
    
    if len(answer) != 0:
        if answer[0] == '.':
            answer = answer[1:]
    
    if len(answer) != 0:
        if answer[-1] == '.':
            answer = answer[:-1]
    
    if len(answer) == 0:
        answer += 'a'
        
    if len(answer) >= 16:
        answer = answer[:15]
            
    if len(answer) != 0:
        if answer[-1] == '.':
            answer = answer[:-1]
            
    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]

    return answer