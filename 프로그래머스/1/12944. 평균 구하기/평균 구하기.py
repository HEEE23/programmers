def solution(arr):
    answer = 0
    count = 0
    for i in arr:
        answer += i
        count += 1
    answer /= count
    return answer