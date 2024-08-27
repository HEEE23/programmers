def solution(elements):
    answer = 0

    # 수열
    seq = []

    elements_len = len(elements)
    
    elements = elements * 2
    for i in range(elements_len):
        for j in range(elements_len):
            seq.append(sum(elements[j:j+i+1]))

    answer = len(set(seq))
    return answer