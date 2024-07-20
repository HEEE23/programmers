def solution(s):
    answer = 0
    
    lst = []
    dic = {}
    s_key = []
    s_value = []
    for i in range(len(s)):
        lst.append(s[i])
        dic[s[i]] = lst.count(s[i])
        
        s_key = list(dic.keys())
        s_value = list(dic.values())
        
        if len(s_value) >= 2:
            if s_value[0] == sum(s_value[1:]):
                answer += 1
                lst = []
                dic = {}
                
    if len(lst) != 0:
        answer += 1          
    return answer