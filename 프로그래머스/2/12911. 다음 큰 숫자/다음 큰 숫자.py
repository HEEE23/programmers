def solution(n):
    answer = 0
    
    # n을 이진 변환했을 때, 1의 갯수
    bin_n = bin(n)[2:].count('1')

    # n보다 큰 자연수 중,
    for i in range(n+1, 1000000):
        # n을 이진 변환했을 때, 1의 갯수가 같은 경우,
        if bin_n == bin(i)[2:].count('1'):
            answer = i
            break
    return answer