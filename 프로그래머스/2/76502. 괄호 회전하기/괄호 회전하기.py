def solution(s):
    answer = 0
    

    for i in range(len(s)-1):
        lst = []
        for j in range(len(s)):
            if s[j] == '[':
                lst.append(s[j])
            elif s[j] == ']':
                if lst == []:
                    lst.append(s[j])
                    break
                else:
                    if lst[-1] != '[':
                        break
                    else:
                        lst.pop()
            elif s[j] == '(':
                lst.append(s[j])
            elif s[j] == ')':
                if lst == []:
                    lst.append(s[j])
                    break
                else:
                    if lst[-1] != '(':
                        break
                    else:
                        lst.pop()
            elif s[j] == '{':
                lst.append(s[j])
            elif s[j] == '}':
                if lst == []:
                    lst.append(s[j])
                    break
                else:
                    if lst[-1] != '{':
                        break
                    else:
                        lst.pop()

        if len(lst) == 0:
            answer += 1

        s = s[1:] + s[0] 

    return answer