def solution(array, height):
    answer = 0
    
    array.sort(reverse = True)
    
    for a in array:
        if a > height:
            answer += 1
        else:
            break
    return answer