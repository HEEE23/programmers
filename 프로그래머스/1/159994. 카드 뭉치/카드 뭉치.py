def solution(cards1, cards2, goal):
    answer = ''
    
    lst = []
    for i in goal:
        if len(cards1) != 0:
            if cards1[0] == i:
                lst.append(cards1[0])
                cards1.remove(cards1[0])
                
        if len(cards2) != 0:
            if cards2[0] == i:
                lst.append(cards2[0])
                cards2.remove(cards2[0])
        
    # for i in range(len(lst)):
    #     if lst[i] == goal[i]:
    #         answer = 'Yes'
    #     else:
    #         answer = 'No'
    
    if lst == goal:
        answer = 'Yes'
    else:
        answer = 'No'
    return answer