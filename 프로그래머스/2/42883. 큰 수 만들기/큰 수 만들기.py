def solution(number, k):
    answer = ''
    
#     number = list(number)
    
#     cnt = 0
#     while cnt != k:
#         for i in range(len(number)):
#             if number[i] > number[i+1]:
#                 num_min = number[i+1]
#                 for j in range(i+2,len(number)):
#                     if number[j] < num_min:
#                         num_min = number[j]
#                     else:
#                         break
#                 number.remove(num_min)
#                 cnt+=1
#                 break
#             elif number[i] < number[i+1]:
#                 number.remove(number[i])
#                 cnt += 1
#                 break

#     answer = ''.join(number)

    stack = []
    for n in number:
        while stack and k > 0 and (stack[-1] < n):
            stack.pop()
            k -= 1

        stack.append(n)
    
    answer = ''.join(stack)
    if k > 0:
        return answer[:-k]
    else:
        return answer
