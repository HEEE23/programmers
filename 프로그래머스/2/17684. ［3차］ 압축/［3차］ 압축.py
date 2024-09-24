def solution(msg):
    answer = []
    
    # 사전
    lzw = {}
    for i in range(26):
        lzw[chr(65+i)] = i + 1
    
    w = c = 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(lzw[msg[w:c]])
            break
        
        # 다음 글자를 포함한 글자가 사전에 없는 경우
        if msg[w:c+1] not in lzw:
            # 사전에 등록
            lzw[msg[w:c+1]] = len(lzw) + 1
            # 색인 번호 출력
            answer.append(lzw[msg[w:c]])
            w = c
        # 사전에 있는 경우, c의 값만 증가
    return answer