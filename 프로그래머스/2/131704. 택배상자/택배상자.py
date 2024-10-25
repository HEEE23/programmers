def solution(order):
    answer = 0
    
    l = len(order)
    num = 0
    stack = []
    while answer < l:
        if order[answer] > num:
            num += 1
            stack.append(num)
        elif order[answer] == stack[-1]:
            stack.pop()
            answer += 1
        else:
            return answer
        
    return answer