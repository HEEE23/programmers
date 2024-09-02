from collections import deque
def solution(cacheSize, cities):
    answer = 0
    
    db = deque()
    
    for c in cities:
        # 대소문자 구분 하지 않음
        c = c.lower()
        if c in db:
            # cache hit일 경우, 실행시간 1
            answer += 1
            db.remove(c)
            db.append(c)

        else:
            # cache miss일 경우, 실행시간 5
            answer += 5
            db.append(c)
        
        # LRU알고리즘 : 가장 오랫동안 참조하지 않은 페이지 교체
        if len(db) > cacheSize:
            db.popleft()
        
    return answer