def solution(brown, yellow):
    answer = []
    
    yellow_x = 0 # 노란색의 가로 길이
    yellow_y = 0 # 노란색의 세로 길이
    
    for i in range(1, yellow+1):
        if yellow % i == 0:
            yellow_x = int(yellow / i)
            yellow_y = i
            
            # 카펫의 가로, 세로 크기 
            if 2 * yellow_x + 2 * yellow_y + 4 == brown: # (x + 2)(y + 2) - xy
                answer.append(yellow_x + 2)
                answer.append(yellow_y + 2)
                break
                
    # 카펫의 가로 길이 >= 세로 길이
    answer.sort(reverse = True)
    return answer