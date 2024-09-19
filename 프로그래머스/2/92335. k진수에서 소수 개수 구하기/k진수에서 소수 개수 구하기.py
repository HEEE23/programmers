import math
def solution(n, k):
    answer = 0
    
    s = ''
    while n > 0:
        n, mod = divmod(n, k)
        s += str(mod)
    
    s = s[::-1]
    
    s = s.split('0')
    
    for ss in s:
        if len(ss) == 0:
            continue
        elif int(ss) < 2:
            continue
        else:
            cnt = 0
            for i in range(2,int(math.sqrt(int(ss)))+1):
                if int(ss) % i == 0:
                    cnt = -1
                    break
            if cnt == 0:
                answer += 1

    return answer