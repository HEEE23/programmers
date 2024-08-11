from collections import defaultdict

def solution(friends, gifts):
    answer = 0
    
    # 각 친구들에게 선물 준 개수
    give_gifts = {f : {j:0 for j in friends if j != f} for f in friends}
    
    exponent = {f : 0 for f in friends}
    for g in gifts:
        give, receive = g.split(' ')
        give_gifts[give][receive] += 1
        exponent[give] += 1
        exponent[receive] -= 1

    for f in friends:
        # 다음달에 받는 선물의 개수
        present = 0
        for ggc in give_gifts[f]:
            # 두 사람이 주고 받은 기록이 없거나 주고받은 수가 같을 때,
            if (give_gifts[f][ggc] == 0 and give_gifts[ggc][f] == 0) or (give_gifts[f][ggc] == give_gifts[ggc][f]):
                # 선물 지수가 더 크면 다음달에 선물 받음
                if exponent[f] > exponent[ggc]:
                    present += 1
            else:
                # 친구에게 선물을 더 많이 줬으면,
                if give_gifts[f][ggc] > give_gifts[ggc][f]:
                    # 다음달에 선물 받음 
                    present += 1
                    
        # 다음달에 가장 많은 선물을 받는 친구가 받을 선물의 수
        answer = max(answer, present)

    return answer