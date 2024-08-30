def solution(n, left, right):
    answer = []

    for i in range(left,right+1):
        arr_max = max(i//n, i%n)
        answer.append(arr_max+1)

    return answer