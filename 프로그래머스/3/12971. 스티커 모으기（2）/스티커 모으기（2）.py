def solution(sticker):
    answer = 0
    
    if len(sticker) == 1:
        return sticker.pop()
    
    # 첫 번째 인덱스를 선택하는 경우
    dp1 = [0] + sticker[:-1]
    for i in range(2, len(sticker)):
        dp1[i] = max(dp1[i-1],dp1[i]+dp1[i-2])
    
    # 두 번째 인덱스를 선택하는 경우
    dp2 = [0] + sticker[1:]
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i-1], dp2[i]+dp2[i-2])
        
    answer = max(dp1[-1],dp2[-1])
    return answer