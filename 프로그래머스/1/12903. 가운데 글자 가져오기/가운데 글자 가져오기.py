def solution(s):
    answer = ''
    print(s[1:3])
    if len(s) % 2 == 0:
        answer = s[int(len(s)/2-1):int(len(s)/2+1)]
    else:
        answer = s[int(len(s)/2)]
            
    return answer 