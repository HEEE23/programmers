def solution(dirs):
    answer = 0
    
    visited = set()
    x,y = 0,0
    
    # 방향
    cmd = {'U' : (0, 1), 'D': (0, -1), 'L' : (-1, 0), 'R' : (1, 0)}
    for d in dirs:
        dx, dy = cmd[d]
        
        nx = x + dx
        ny = y + dy
        
        if abs(nx) <= 5 and abs(ny) <= 5:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            
            x, y = nx, ny
            
    answer = len(visited) // 2
    return answer