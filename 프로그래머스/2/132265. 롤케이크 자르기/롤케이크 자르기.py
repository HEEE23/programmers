from collections import Counter
def solution(topping):
    answer = 0
    
#     # 시간초과
#     for i in range(len(topping)):
#         t1 = set(topping[:i+1])
#         t2 = set(topping[i+1:])
        
#         if len(t1) == len(t2):
#             answer += 1
            
#         if len(t1) > len(t2):
#             break
      
    dic = Counter(topping)
    # 동생
    set_dic = set()
    
    for t in topping:
        dic[t] -= 1
        set_dic.add(t)

        if dic[t] == 0:
            dic.pop(t)
        
        if len(set_dic) == len(dic):
            answer += 1
    
    return answer