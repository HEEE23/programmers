def solution(s):
    answer = 1000
    
    for l in range(1,len(s)+1):
        ss = []
        cnt = 1
        for i in range(0, len(s)+1, l):
            if s[i:i+l] == s[i+l:i+l+l]:
                cnt += 1
            else:
                ss.append(str(cnt))
                ss.append(s[i:i+l])
                cnt = 1
                
        if '1' in ss:
            while '1' in ss:
                ss.remove('1')
        
        ss = ''.join(ss)
        answer = min(answer,len(ss))
        
    return answer