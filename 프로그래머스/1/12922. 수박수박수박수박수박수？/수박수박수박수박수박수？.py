def solution(n):
    answer = ''
    result = []
    for i in range(n):
        if i%2 == 0:
            result.append('수')
        else:
            result.append('박')
    answer = ''.join(result)
    return answer