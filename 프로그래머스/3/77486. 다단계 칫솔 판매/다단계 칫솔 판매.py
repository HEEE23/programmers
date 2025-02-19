def solution(enroll, referral, seller, amount):
    answer = []
    
    amount = [a*100 for a in amount]
    
    enroll2 = {}
    for i in range(len(enroll)):
        enroll2[enroll[i]] = i
        
    # center 민호 포함 이득
    profit = [0]*(len(enroll))
    for i in range(len(seller)):
        s = [seller[i]]
        a = amount[i]

        while s:
            sell = s.pop(0)
            idx = enroll2[sell]
            
            # '-'인 경우, 민호 아래 판매원이기 때문에 반복문 종료
            if referral[idx] == '-':
                profit[idx] += a - int(a*0.1)
                break
            # '-'가 아닌 경우, 추천인이 남아있기 때문에 리스트에 추가
            else:              
                profit[idx] += a - int(a*0.1)
                
                a = int(a*0.1)
                # 이익이 0원인 경우, 분배할 게 없기 때문에 반복문 종료
                if a == 0:
                    break
                    
                s.append(referral[idx])
                
    answer = profit

    return answer