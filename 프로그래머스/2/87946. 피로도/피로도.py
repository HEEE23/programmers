# 순열 이용
from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    for p in permutations(dungeons, len(dungeons)):
        tmp = k
        cnt = 0
        for need, consume in p:
            if tmp >= need:
                tmp -= consume
                cnt += 1
        answer = max(cnt, answer)
    
    return answer