def solution(my_string, is_prefix):

    prefix = []
    for i in range(1,len(my_string)):
        prefix.append(my_string[:i])
    
    if is_prefix in prefix:
        answer = 1
    else:
        answer = 0
        
    return answer