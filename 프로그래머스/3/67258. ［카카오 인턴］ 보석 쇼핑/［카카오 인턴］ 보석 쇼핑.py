def solution(gems):
    answer = [0, len(gems)]
    
    # 투 포인터 사용
    left, right = 0, 0
    
    # 진열된 보석의 개수
    cnt = len(set(gems))
    
    jewel = {gems[0] : 1}
    while left < len(gems) and right < len(gems):
        # 딕셔너리 안에 모든 종류의 보석이 있으면,
        if len(jewel) == cnt:
            # 최소 크기면, answer 갱신
            if right-left < answer[1] - answer[0]:
                answer = [left, right]
            else:
                # 가장 짧은 구간 찾기 위해, 보석 제거
                jewel[gems[left]] -= 1
                
                # 보석이 없으면, 딕셔너리에서 제거
                if jewel[gems[left]] == 0:
                    del jewel[gems[left]]
                    
                left += 1
                
        # 딕셔너리 안에 모든 종류의 보석이 없으면, 보석 추가
        else:
            right += 1
            
            if right == len(gems):
                break
                
            if gems[right] in jewel:
                jewel[gems[right]] += 1
            else:
                jewel[gems[right]] = 1   
                
    return [answer[0]+1, answer[1]+1]