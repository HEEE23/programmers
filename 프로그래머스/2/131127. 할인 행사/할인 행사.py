def solution(want, number, discount):
    answer = 0
    
    # 정현이가 원하는 제품과 수량
    want_dic = {}
    for i in range(len(want)):
        want_dic[want[i]] = number[i]

    lst = []
    for i in range(len(discount)-9):
        # 10일 연속 할인하는 제품과 수량
        lst = discount[i:i+10]
        discount_dic = {}
        for j in range(len(lst)):
            if lst[j] in discount_dic:
                discount_dic[lst[j]] += 1
            else:
                discount_dic[lst[j]] = 1
        
        cnt = 0
        for w in want:
            if w not in discount_dic:
                break
            else:
                if want_dic[w] <= discount_dic[w]:
                    cnt += 1
        
        if cnt == len(want):
            answer += 1
                
    return answer