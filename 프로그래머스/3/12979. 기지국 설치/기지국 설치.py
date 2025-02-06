from collections import deque
def solution(n, stations, w):
    # 현재 위치, 기지국 개수의 최솟값
    now, answer = 1, 0
    
    q = deque(stations)
    while 1:
        if now > n:
            break
        # 설치된 기지국이 남아있는 경우
        if q:
            # 현재 위치가 설치된 기지국 범위 안에 들어 있는 경우
            if now >= q[0]-w and now <= q[0]+w:
                # 설치된 기지국 오른쪽 끝으로 이동
                now = q.popleft() + w + 1
                continue
        else:
            # 현재 위치의 최대 전달 범위가 n을 넘어가면 종료
            if now + w > n:
                answer += 1
                break
                
        # 현재 위치에 기지국 설치 후 오른쪽 끝으로 이동
        now += (w*2 + 1)
        answer += 1
            
    return answer