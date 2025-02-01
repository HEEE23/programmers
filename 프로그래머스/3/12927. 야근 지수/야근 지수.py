import heapq
def solution(n, works):
    answer = 0
    
    if sum(works) < n:
        return 0
    
    heap = []
    for w in works:
        heapq.heappush(heap, -w)
    
    while n != 0:
        work = -heapq.heappop(heap)
        work -= 1
        heapq.heappush(heap, -work)
        n -= 1

    for h in heap:
        answer += h**2
        
    
#     # 효율성 테스트 실패
#     while n != 0:
#         works.sort(reverse = True)
#         if works[0] > 0:
#             works[0] -= 1
#         n -= 1
    
#     for w in works:
#         answer += w**2

    return answer