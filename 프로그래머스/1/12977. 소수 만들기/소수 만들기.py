def solution(nums):
    answer = -1

    from itertools import combinations
    lst = list(combinations(nums,3))
    
    for i in range(len(lst)):
        lst[i] = sum(lst[i])
    
    result = []
    for l in lst:
        count = 0
        for i in range(1,  int(l**(1/2))+1):
            if l%i == 0:
                count += 1
                if (i**2) != l:
                    count += 1
        if count == 2:
            result.append(l)
    answer = len(result)
    return answer