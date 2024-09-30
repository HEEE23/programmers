from collections import deque
def solution(numbers):
#     # 시간초과
#     answer = []
    
#     q = deque(numbers)

#     while len(q) != 0:
#         num = q.popleft()

#         cnt = 0
#         for n in q:
#             if n > num:
#                 answer.append(n)
#                 cnt += 1
#                 break
#         if cnt == 0:
#             answer.append(-1)
    
    answer = [-1]*len(numbers)
    
    stack = []
    for i in range(len(numbers)):
        target = numbers[i]
        
        # 스택에 값이 있고 뒷 큰수를 만났으면, answer에 담음
        while stack and numbers[stack[-1]] < target:
            answer[stack.pop()] = target
        
        # 스택에 값이 없고 뒷 큰수 역할을 못하면 stack에 담음
        stack.append(i)
    return answer