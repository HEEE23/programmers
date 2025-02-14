import heapq
def solution(jobs):
    answer = 0
    
    time = 0 # 현재시간
    cnt = 0 # 처리 개수
    start = -1 # 마지막 완료시간
    
    heap = []
    while cnt < len(jobs):
        
        for job in jobs:
            if start < job[0] <= time:
                heapq.heappush(heap, [job[1],job[0]])
                
        if heap:
            current = heapq.heappop(heap)
            start = time
            time += current[0]
            
            answer += time - current[1]
            cnt += 1
        else:
            time += 1
            
    answer //= len(jobs)
    
#     # 실패
#     jobs = sorted(jobs, key = lambda x : x[1])

#     for i in range(len(jobs)):
#         jobs[i] = [jobs[i][1], jobs[i][0]]

#     end, request = 0,0

#     heap = []
#     heapq.heappush(heap,jobs.pop(0))
    
#     time = 0
#     returnTime = []
#     while heap:
#         if end == time:
#             end, request = heapq.heappop(heap)
#             end, start = end + time, time
#             returnTime.append(end-request)
            
#         time += 1
        
#         if jobs:
#             if time == jobs[0][1]:
#                 heapq.heappush(heap, jobs.pop(0))

#     answer = int(sum(returnTime)/len(returnTime))

    return answer