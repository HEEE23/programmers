def solution(N, number):
    # 최소값이 8보다 크면 -1 
    answer = -1
    arr = [set() for i in range(8)]
    
    # N이 number이면 경우의 수 1
    if number == N:
        return 1
    
    # {N}, {NN}, {NNN}, ...
    for i in range(len(arr)):
        arr[i].add(int(str(N)*(i+1)))
    
    # N을 사용한 횟수가 i+1일 때, 사칙연산을 사용해서 만들 수 있는 숫자
    for i in range(1, 8):
        for j in range(i):
            for op1 in arr[j]:
                for op2 in arr[i-j-1]:
                    arr[i].add(op1+op2)
                    arr[i].add(op1-op2)
                    arr[i].add(op1*op2)
                    if op2 != 0:
                        arr[i].add(op1//op2)
                        
        if number in arr[i]:
            answer = i+1
            break
            
    return answer