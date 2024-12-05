import heapq
def solution(n, k, enemy):
    answer, sume = 0,0
    
    heap = []
    for e in enemy:
        heapq.heappush(heap, -e)
        sume += e
        if sume > n:
            if k == 0:
                break
            sume += heapq.heappop(heap)
            k -= 1
        answer += 1
    return answer