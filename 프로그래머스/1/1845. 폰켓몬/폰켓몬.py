def solution(nums):
#     from itertools import combinations
#     answer = 0
    
#     h = int(len(nums)/2)
#     lst = list(combinations(nums, h))
    
#     result = []
#     for i in lst:
#         result.append(len(list(set(i))))
    
#     answer = max(result)
    answer = 0
    result = list(set(nums))
    
    print(result)
    if len(result) > int(len(nums)/2):
        answer = int(len(nums)/2)
    else:
        answer = len(result)
    return answer