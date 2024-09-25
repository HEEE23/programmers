from itertools import product
def solution(word):
    answer = 0
    
    alp = ['A','E','I','O','U']
    
    lst = []
    for i in range(1,6):
        for p in product(alp,repeat = i):
            lst.append(''.join(p))
    
    lst.sort()
    answer = lst.index(word)+1
            
    return answer