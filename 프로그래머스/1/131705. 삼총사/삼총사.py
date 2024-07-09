from itertools import combinations
def solution(number):
    answer = 0
    
    lst = list((combinations(number,3)))
    
    count = 0
    for i in range(len(lst)):
        if sum(lst[i]) == 0:
            count += 1
    answer = count
    return answer