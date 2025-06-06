def solution(number):
    answer = 0
    
    number = list(map(int,number))
    
    answer = sum(number) % 9
    return answer