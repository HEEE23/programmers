def solution(n, k, cmd):
    answer = ''
    
    # 링크드리스트 사용
    # 해당 인덱스 : [앞 인덱스, 뒷 인덱스] 연결
    liked_lst = {i : [i-1, i+1] for i in range(n)}
    table = ['O']*n
    delete = []

    for c in cmd:
        c = c.split()
        
        if c[0] == 'U':
            for _ in range(int(c[1])):
                k = liked_lst[k][0] 
                
        elif c[0] == 'D':
            for _ in range(int(c[1])):
                k = liked_lst[k][1]
                
        elif c[0] == 'C':
            prev, nxt = liked_lst[k]
            table[k] = 'X'
            delete.append((prev, k, nxt))
            
            # 마지막 행인 경우, 바로 윗 행 선택
            if nxt == n:
                k = liked_lst[k][0]
            else:
                k = liked_lst[k][1]
            
            #  지울 행이 첫 번째 행인 경우, 그 다음 행 연결 정보만 변경 
            if prev == -1:
                liked_lst[nxt][0] = prev
            # 지울 행이 마지막 행인 경우, 그 이전 행 연결 정보만 변경
            elif nxt == n:
                liked_lst[prev][1] = nxt
            # 앞 뒤 행의 연결 정보 변경
            else:
                liked_lst[prev][1] = nxt
                liked_lst[nxt][0] = prev
        else:
            prev, now, nxt = delete.pop()
            
            # 변경한 정보를 다시 복구
            table[now] = 'O'
            
            if prev == -1:
                liked_lst[nxt][0] = now
            elif nxt == n:
                liked_lst[prev][1] = now
            else:
                liked_lst[prev][1] = now
                liked_lst[nxt][0] = now
                
    answer = ''.join(table)
            
    return answer