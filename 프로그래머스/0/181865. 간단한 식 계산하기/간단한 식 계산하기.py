def solution(binomial):
    answer = 0
    a, op, b = binomial.split()
    
    if op == '+': return int(a) + int(b)
    elif op == '-': return int(a) - int(b)
    elif op == '*': return int(a) * int(b)  

    return answer