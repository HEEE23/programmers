from collections import deque
def solution(n, m, x, y, r, c, k):
    answer = ''
    
    def distance(x, y, r, c):
        return abs(x-r) + abs(y-c)
    
    def bfs():
        q = deque([])
        q.append([x, y, 0, ''])

        while q:
            a, b, cnt, s = q.pop()
            if a == r and b == c:
                if cnt == k:
                    return s
                elif (k-cnt) % 2 == 1:
                    return 'impossible'

            lst = []
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]

                if 0 < nx <= n and 0 < ny <= m and distance(nx, ny, r, c) + cnt < k:
                    lst.append([nx, ny, cnt + 1, s + dirs[i]])

            lst.reverse()
            q += lst

        return 'impossible'
    
    # 사전순 d, l, r, u, 
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    
    dirs = ['d','l','r','u']
    
    answer = bfs()
    return answer