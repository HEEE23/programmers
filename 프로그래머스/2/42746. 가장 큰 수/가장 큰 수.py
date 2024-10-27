from itertools import permutations
def solution(numbers):
    answer = ''
    
    # lst = list(permutations(numbers, len(numbers)))
    # lst1 = []
    # for l in lst:
    #     lst1.append(''.join(map(str,l)))
    # answer = max(lst1)
    
    numbers = list(map(str,numbers))
    numbers.sort(key = lambda x:x*3, reverse=True)
    answer = str(int(''.join(numbers)))
    return answer