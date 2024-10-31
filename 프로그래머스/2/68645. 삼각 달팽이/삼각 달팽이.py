def solution(n):
    answer = []
    
    lst = []
    for i in range(n):
        l = []
        for j in range(i+1):
            l.append(0)
        lst.append(l)
        
    # 방향 : 아래, 오른쪽, 왼쪽위
    dirs = [(1,0),(0,1),(-1,-1)]
    turn = 0
    
    # 현재 위치
    a, b = 0, 0
    for i in range(1, int((n**2+n)/2)+1):
        lst[a][b] = i
        dx, dy = dirs[turn]
        
        nx = a + dx
        ny = b + dy
        
        # 0 이거나 범위안에 있는 경우
        if 0 <= nx < n and 0 <= ny < n and lst[nx][ny] == 0:
            a, b = nx, ny
        # 0이 아니거나 범위를 벗어날 경우
        else:
            turn = (turn + 1) % 3
            dx, dy = dirs[turn]
        
            a += dx
            b += dy
    
    for ll in lst:
        answer.extend(ll)

    return answer