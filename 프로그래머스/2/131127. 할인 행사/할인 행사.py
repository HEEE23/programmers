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
        
        # 정현이가 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치하는 경우
        if want_dic == discount_dic:
            answer += 1
                
    return answer