def solution(s):
    answer = True
    
    stack = []
    for i in s:
        # i == '('이면,
        if i == '(':
            stack.append('(')
        
        # i == ')'이면,
        else: 
            if stack == []:
                return False
            else:
                stack.pop()
                
    if stack != []:
        return False
    return True