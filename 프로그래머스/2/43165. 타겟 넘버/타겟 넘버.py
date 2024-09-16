def solution(numbers, target):
    answer = 0
    
    lst = [0]
    for num in numbers:
        res = []
        for l in lst:
            res.append(l+num)
            res.append(l-num)
        lst = res

    answer = lst.count(target)
        
    return answer