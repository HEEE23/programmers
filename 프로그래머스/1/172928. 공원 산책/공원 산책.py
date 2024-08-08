def solution(park, routes):
    answer = [0,0]
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                S = [i,j]
                break
    a = []
    b = []
    for r in routes:
        x, y = r.split(' ')
        a.append(x)
        b.append(int(y))

    X = []
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'X':
                X.append([i,j])

    for i in range(len(a)):
        if a[i] == 'E':
            answer[1] = S[1] + b[i]
            answer[0] = S[0]
            if answer[1] >= len(park[0]):
                answer[1] = S[1]   
            else:
                if len(X) != 0:
                    for xx in X:
                        if xx[0] == S[0]:
                            if xx[1] > S[1] and xx[1] <= answer[1]:                                      
                                answer[1] = S[1]
            S[1] = answer[1]    
                    
        elif a[i] == 'W':
            answer[1] = S[1] - b[i]
            answer[0] = S[0]
            if answer[1] < 0:
                answer[1] = S[1]
            else:
                if len(X) != 0:
                    for xx in X:
                        if xx[0] == S[0]:
                            if xx[1] >= answer[1] and xx[1] < S[1]:                                      
                                answer[1] = S[1]
            S[1] = answer[1]
            
        elif a[i] == 'S':
            answer[0] = S[0] + b[i]
            answer[1] = S[1]
            if answer[0] >= len(park):
                answer[0] = S[0]
            else:
                if len(X) != 0:
                    for xx in X:
                        if xx[1] == S[1]:
                            if xx[0] > S[0] and xx[0] <= answer[0]:                                      
                                answer[0] = S[0]
            S[0] = answer[0]
            
        elif a[i] == 'N':
            answer[0] = S[0] - b[i]
            answer[1] = S[1]
            if answer[0] < 0:
                answer[0] = S[0]
            else:
                if len(X) != 0:
                    for xx in X:
                        if xx[1] == S[1]:
                            if xx[0] >= answer[0] and xx[0] < S[0]:                                      
                                answer[0] = S[0]
            S[0] = answer[0]
        print(answer)
    return answer