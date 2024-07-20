def solution(participant, completion):
    answer = ''
    
#     for c in completion:
#         if c in participant:
#             participant.remove(c)
            
#     answer = ''.join(participant)
    
    dic = {}
    for p in participant:
        dic[p] = dic.get(p, 0) + 1  # 기본값 0
    
    
    for c in completion:
        dic[c] -= 1
        
    for k, v in dic.items():
        if v > 0:
            answer = k

    return answer