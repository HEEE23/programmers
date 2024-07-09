def solution(s):
    answer = []
    s = list(s)
    result = {}
    for i in range(len(s)):
        if s[i] in result:
            answer.append(i-result[s[i]])
        else:
            answer.append(-1)
        result[s[i]] = i
    return answer