def solution(number, limit, power):
    answer = 0

    for num in range(1,number+1):
        count = 0
        for i in range(1, int(num**(1/2))+1):
            if num % i == 0:
                count+=1
                if (i**2) != num:
                    count+=1
        if count > limit:
            count = power
        answer += count
    return answer