def solution(scores):
    answer = 1
    
    wanho = scores[0]
    wanho_score = sum(wanho)
    
    scores = sorted(scores, key = lambda x : (-x[0], x[1]))

    tmp = 0
    for a, b in scores:
        if wanho[0] < a and wanho[1] < b:
            return -1

        if wanho_score < (a+b) and tmp <= b:
            answer += 1
            tmp = b
        
    return answer

# # 시간초과
# def incentive(s, scores):
#     A, B = s[0], s[1]
    
#     for score in scores:
#         a, b = score[0], score[1]
#         if A < a and B < b:
#             return False
        
#     return True

# def solution(scores):
#     answer = 0
    
#     won = [sum(scores[0])]
#     for i in range(len(scores)):
#         # 인센티브 여부 확인
#         incen = incentive(scores[i], scores)
#         if not incen:
#             if i == 0:
#                 return -1
#         else:
#             if i > 0:
#                 if won[0] <= sum(scores[i]):
#                     won.append(sum(scores[i]))

#     sorted_score = sorted(won, reverse = True)
#     answer = sorted_score.index(won[0])+1
    
#     return answer