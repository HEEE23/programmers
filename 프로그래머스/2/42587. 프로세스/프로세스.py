def solution(priorities, location):
    answer = 0
    
    l = priorities.index(max(priorities))
    while True:
        value = max(priorities)
        
        if value == priorities[l]:
            answer += 1
            priorities[l] = 0
            if l == location:
                break
        else:
            l += 1
            if l >= len(priorities):
                l = 0
            
    return answer