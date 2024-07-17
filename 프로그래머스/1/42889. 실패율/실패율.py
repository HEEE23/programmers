def solution(N, stages):
    answer = []
    
    fail = {}
    users = len(stages)
    for i in range(1, N+1):
        u = len(list(filter(lambda x : x == i, stages)))
        if users != 0:
            fail[i] = u / users
            users -= u
        else:
            fail[i] = 0

    answer = sorted(fail, key = lambda x : fail[x], reverse = True)
    return answer