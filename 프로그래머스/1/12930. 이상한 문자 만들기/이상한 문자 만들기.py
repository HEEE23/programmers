def solution(s):
    answer = ''
    
    s = list(s.split(" "))

    for str in s:
        for i in range(len(str)):
            if i%2 == 0:
                answer += str[i].upper()
            else:
                answer += str[i].lower()
        answer+=' '
    return answer[:-1]