def solution(babbling):
    answer = 0
    pron = ['aya','ye','woo','ma']
    
    for b in babbling:
        for p in pron:
            if p*2 not in b:
                b = b.replace(p,' ')
                
        if b.isspace():
             answer += 1   
                
    return answer