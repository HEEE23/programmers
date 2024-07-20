def solution(keymap, targets):
    answer = []
    keymap = list(list(k) for k in keymap)
    
    for t in targets:
        press = 0
        for i in range(len(t)):
            lst = []
            for k in keymap:
                if t[i] in k:   
                    lst.append(k.index(t[i]))
                else:
                    lst.append(10000)
            press += (min(lst)+1)
            
        if press >= 10001:
            answer.append(-1)
        else:
            answer.append(press)

    return answer
