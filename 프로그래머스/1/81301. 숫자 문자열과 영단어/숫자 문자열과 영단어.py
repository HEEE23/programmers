def solution(s):
    answer = 0
    dic = {'zero': 0, 'one': 1,'two' : 2 , 'three' : 3, 'four' : 4, 
           'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}

    dic_k = list(dic.keys())
    
    for i in range(len(dic_k)):
        if dic_k[i] in s:
            s = s.replace(dic_k[i], str(dic[dic_k[i]]))
    answer = int(s)
    return answer