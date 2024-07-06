def solution(absolutes, signs):
    answer = 123456789
    signs_i = []

    for i in range(len(signs)):
        if signs[i] == False:
            signs_i.append(i)

    for i in signs_i:
        absolutes[i] = -absolutes[i]
        
    answer = sum(absolutes)
    return answer
    