def solution(X, Y):
    answer = ''
    
    dic_x = {}
    dic_y = {}
    for i in X:
        dic_x[i] = dic_x.get(i,0)+1

    for i in Y:
        dic_y[i] = dic_y.get(i,0)+1
    
    key = sorted(dic_x, reverse = True)    
    for k in key:
        if k in dic_y:
            for i in range(min(dic_x[k],dic_y[k])):
                answer += k
                
    result = {}
    for a in answer:
        result[a] = result.get(a,0)+1
        
    answer_key = sorted(result, reverse = True)

    if len(answer) == 0:
        answer = '-1'
    elif len(answer_key) == 1:
        if '0' in answer_key:
            answer = '0'
                    
    return answer