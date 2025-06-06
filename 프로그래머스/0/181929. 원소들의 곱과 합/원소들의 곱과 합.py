def solution(num_list):
    s = 0
    mul = 1
    for n in num_list:
        s += n
        mul *= n
        
    if mul < s**2:
        answer = 1
    else:
        answer = 0
        
    return answer