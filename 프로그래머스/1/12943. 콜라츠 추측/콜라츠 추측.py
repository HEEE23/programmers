def solution(num):
    answer = 0
    count = 0
    
    while count != 500:
        if num == 1:
            break
        else:
            count += 1 
            if num % 2 == 0:
                num /= 2
            else:
                num = (num*3) + 1
    if count == 500:
        answer = -1
    else:
        answer = count
    
    return answer