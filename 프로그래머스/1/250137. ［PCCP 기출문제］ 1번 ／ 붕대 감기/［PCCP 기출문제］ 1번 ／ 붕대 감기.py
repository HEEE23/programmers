def solution(bandage, health, attacks):
    answer = health
    
    # 몬스터의 마지막 공격
    a = attacks[len(attacks)-1][0]
    
    # 최대체력
    max_h = health 
    
    count = 0
    for i in range(a+1): 
        # 몬스터에게 공격 당함
        if attacks[0][0] == i:
            answer -= attacks[0][1]
            # 체력이 0 이하가 되면, -1을 return
            if answer <= 0:
                answer = -1
                count = 0
                break
            else:
                attacks.pop(0)
                # 연속 성공 시간 초기화
                count = 0
        # 몬스터에게 공격 당하지 않음
        else:
            # 체력이 줄어들었으면,
            if answer < max_h:
                # [초당 회복량] 만큼 체력 추가 회복
                answer += bandage[1]
                if answer >= max_h:
                    answer = max_h
            # 붕대 연속 감기
            if i > 0:
                count += 1
            # [시전 시간]만큼 성공하면 체력을 [추가 회복량]만큼 추가 회복
            if count == bandage[0]:
                if answer < max_h:
                    answer += bandage[2]
                if answer >= max_h:
                    answer = max_h
                # 연속 성공 초기화
                count = 0

    return answer