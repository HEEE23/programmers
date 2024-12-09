from itertools import combinations

def solution(relation):
    rows = len(relation)
    cols = len(relation[0])
    
    # 유일성
    unique = []
    for i in range(1,cols+1):
        unique.extend(combinations(range(cols),i))

    result = []
    for u in unique:
        t = [tuple([r[idx] for idx in u]) for r in relation]

        if len(set(t)) == rows:
            result.append(u)

    answer = set(result)
    # 최소성
    for i in range(len(result)):
        for j in range(i+1, len(result)):
            if len(result[i]) == len(set(result[i]) & set(result[j])):
                answer.discard(result[j])
                
    return len(answer)