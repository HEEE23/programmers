def solution(s):
    answer = ''
    
    s = s.lower()
    
    lst = s.split(' ')
    for i in range(len(lst)):
        if lst[i].isalpha() == True:
            lst[i] = lst[i].capitalize()
            
    answer = ' '.join(lst)
    return answer