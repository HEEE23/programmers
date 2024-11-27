def check(s):
    stack = []

    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return True

def divide(s):
    dic = {'(':0, ')':0}
    
    for i in range(len(s)):
        if s[i] == '(':
            dic[s[i]] += 1
        else:
            dic[s[i]] += 1
        
        if dic['('] == dic[')']:
            return s[:i+1], s[i+1:]

def solution(p):
    if not p:
        return ''

    u, v = divide(p)

    # u가 올바른 괄호 문자열이라면
    if check(u):
        return u + solution(v)
    # u가 올바른 괄호 문자열이 아니라면
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        
        for s in u[1:len(u)-1]:
            if s == '(':
                answer += ')'
            else:
                answer += '('
    return answer