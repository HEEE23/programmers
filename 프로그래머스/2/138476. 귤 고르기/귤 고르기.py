from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    
    dic = defaultdict(int)
    
    # 각 귤의 크기 별 개수
    for t in tangerine:
        dic[t] += 1
    cnt = sorted(dic.values(), key = lambda x : -x)
    
    # 담은 귤의 개수
    num = 0
    for c in cnt:
        if num < k:
            num += c
            answer += 1
        else:
            return answer
    return answer