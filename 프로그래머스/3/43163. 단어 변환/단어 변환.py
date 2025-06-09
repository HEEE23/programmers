from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    
    return bfs(begin, target, words)

def bfs(begin, target, words):
    answer = 0
    
    queue = deque()
    step = 0
    queue.append([begin,step])
    while queue:
        now, step = queue.popleft()
        
        if now == target:
            answer = step
            break
            
        for w in words:
            cnt = 0
            for i in range(len(now)):
                if w[i] != now[i]:
                    cnt += 1
            if cnt == 1:
                queue.append([w, step+1])

    return answer
    