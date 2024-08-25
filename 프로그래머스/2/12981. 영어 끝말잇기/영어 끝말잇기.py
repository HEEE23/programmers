def solution(n, words):
    answer = []
    
    chain = []
    
    cnt = 1 # 차례
    num = 0 # 사람 번호
    for i in range(len(words)):
        num += 1
        
        # 다음 차례 
        if num > n:
            cnt += 1
            num = 1
        
        # 이전에 등장했던 단어 사용
        if words[i] in chain:
            answer.append(num)
            answer.append(cnt)
            break
            
        chain.append(words[i])
        
        if len(chain) > 1:
            # 앞 사람이 말한 단어의 마지막 문자로 시작하는 단어로 말한 경우
            if chain[i-1][-1] == chain[i][0]:
                continue
            # 아닌 경우
            else:
                answer.append(num)
                answer.append(cnt)
                break
    
    # 탈라자가 생기지 않는다면, [0,0] 리턴
    if len(answer) == 0:
        answer.extend([0,0])

    return answer