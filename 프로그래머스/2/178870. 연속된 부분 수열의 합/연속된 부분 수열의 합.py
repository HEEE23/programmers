def solution(sequence, k):
    num = 0
    for i in range(len(sequence)-1, -1, -1):
        num += sequence[i]

        if num > k:
            num -= sequence.pop() 
        if num == k:
            while sequence[i-1] == sequence[-1] and i>0:
                i-=1
                sequence.pop()

            return [i, len(sequence)-1]
        
# # 방법 1. 시간초과
# def solution(sequence, k):
#     answer = []
    
#     stack = []

#     for i in range(len(sequence)):
#         lst = []
#         p = 0
#         for j in range(i,len(sequence)):
#             p += sequence[j]
#             lst.append((sequence[j],j))
#             if p == k:
#                 stack.append(lst)
#                 break
#             elif p > k:
#                 break
    
#     print(stack)
#     len_min = len(stack[0])
#     idx = 0
#     for i in range(1,len(stack)):
#         if len(stack[i]) < len_min:
#             len_min = len(stack[i])
#             idx = i

    
#     answer.extend([stack[idx][0][1],stack[idx][-1][1]])
    
#     return answer