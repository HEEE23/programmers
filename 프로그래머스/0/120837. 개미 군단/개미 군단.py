def solution(hp):
    answer = 0
    
    while (hp!=0):
        if hp >= 5:
            answer += hp//5
            hp %= 5
        elif hp >= 3:
            answer += hp//3
            hp %= 3
        elif hp >= 1:
            answer += 1
            hp -= 1
            
    return answer