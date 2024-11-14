from functools import reduce
import math

def solution(arrayA, arrayB):
    answer = 0

    lst = [reduce(math.gcd,arrayA)]
    lst.append(reduce(math.gcd,arrayB))

    a = 1
    b = 1
    for i in range(len(arrayA)):
        if arrayA[i] % lst[1] == 0:
            a = 0
        if arrayB[i] % lst[0] == 0:
            b = 0
    
    if a == 0 and b == 0:
        return 0
    
    return max(lst)

#     # 시간초과 
#     num = set()
#     for i in range(2, max(arrayA[0], arrayB[0])+1):
#         if arrayA[0] % i == 0 or arrayB[0] % i == 0:
#             num.add(i)

#     num = sorted(num, reverse = True)        
    
#     for n in num:
#         cnt1 = 0
#         cnt2 = 0
#         for i in range(len(arrayA)):
#             if arrayA[i] % n == 0 and arrayB[i] % n != 0:
#                 cnt1 += 1
#             elif arrayB[i] % n == 0 and arrayA[i] % n != 0:
#                 cnt2 += 1
                
#         if cnt1 == len(arrayA) or cnt2 == len(arrayA):
#             answer = n
#             break
    
    
#     return answer