def solution(numbers):
    answer = -1
    numbers.sort()
    lst = []

    for i in range(10):
        if i not in numbers:
            lst.append(i)
    answer = sum(lst)
    return answer