from itertools import permutations
def solution(numbers):
    answer = 0
    
    per_numbers = []
    for i in range(1,len(numbers)+1):
        per_numbers.extend(list(permutations(numbers,i)))
        
    lst = []
    for n in per_numbers:
        lst.append(int(''.join(n)))

    lst = set(lst)
    for l in lst:
        if l < 2:
            continue

        ck = True     
        for i in range(2,int(l**0.5)+1):
            if l % i == 0:
                ck = False
                break
        if ck:
            answer += 1

    return answer