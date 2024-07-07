def solution(price, money, count):
    answer = -1
    result = 0
    for i in range(1,count+1):
        result += price*i
    if money > result:
        answer = 0
    else:
        answer = (result-money)
    return answer