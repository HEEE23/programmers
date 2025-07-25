def solution(stones, k):
    answer = 0
    
    left = 1
    right = max(stones)
    
    while left <= right:
        mid = (left+right) // 2
        print(mid)
        ni = 0
        for s in stones:
            if s - mid < 0:
                ni +=1 
            else:
                ni = 0
                
            if ni >= k:
                break
        
        if ni >= k:
            right = mid -1
        else:
            answer = mid
            left = mid + 1
    return answer
# def solution(stones, k):
#     answer = 0
    
#     # 이진 탐색 
#     start = 1
#     end = max(stones)
    
#     while start <= end:
#         cnt = 0
#         # 건너는 인원
#         mid = (start + end) // 2

#         for stone in stones:
#             if (stone - mid) <= 0:
#                 cnt += 1
#                 if cnt >= k:
#                     break
#             else:
#                 cnt = 0
            
#         if cnt < k:
#             start = mid + 1
#         else:
#             answer = mid
#             end = mid - 1
    
# #     # 정확성만 통과, 효율성 x
# #     while True:
# #         cnt = 0
# #         answer += 1   
        
# #         for i in range(len(stones)):
# #             if stones[i] != 0:
# #                 stones[i] -= 1
# #             else:
# #                 continue
        
# #         for stone in stones:
# #             if stone == 0:
# #                 cnt += 1
# #                 if cnt == k:
# #                     return answer
# #             else:
# #                 cnt = 0

#     return answer
