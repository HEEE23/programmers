def solution(s):
    answer = 0

    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                answer = max(answer, len(s[i:j]))
    
#     # 실패
#     a = 0
#     while a != len(s):
#         cnt = 0
#         l = len(s[:a])
        
#         for i in range(a+1):
#             if i-l+1 > 0:
#                 if s[i-l+1] == s[i]:
#                     cnt += 1

#         if (a+1)%2 != 0:
#             if cnt == (len(s)//2):
#                 answer = a+1

#         a += 1
                
    return answer