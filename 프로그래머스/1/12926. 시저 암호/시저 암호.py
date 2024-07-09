def solution(s, n):
    answer = ''
    s = list(s)
    
    result = 0
    for alp in s:
        if 65 <= ord(alp) and ord(alp) <= 90:
            result = ord(alp)+n
            if result > 90:
                result = result-26
            answer += chr(result)
        elif alp == ' ':
            answer += ' '
        
        else:
            result = ord(alp)+n
            if result > 122:
                result = result - 26
            answer += chr(result)
        
    return answer