def solution(storey):
    answer = 0
    
    while storey:
        s = storey % 10
        if s > 5:
            answer += (10 - s)
            storey += 10
        elif s < 5:
            answer += s
        else:
            if (storey//10)%10 > 4:
                storey += 10
            answer += s
        storey //= 10
        
#     # 실패 
#     s = str(storey)
#     sl = len(s)
    
#     dic = {}
#     a = len(s)
#     for i in range(sl):
#         dic[i] = a - 1
#         a -= 1

#     for i in range(sl-1,-1,-1):
#         if int(s[i]) != 0:
#             if 10 - int(s[i]) <= int(s[i]):
#                 answer += 10 - int(s[i])
#                 storey += 10**(dic[i]) * (10 - int(s[i]))
#             else:
#                 answer += int(s[i])
#                 if i != 0:
#                     storey -= 10**(dic[i]) * int(s[i])
        
#         s = str(storey)

#     if sl != len(s):
#         answer += int(s[0])

    return answer