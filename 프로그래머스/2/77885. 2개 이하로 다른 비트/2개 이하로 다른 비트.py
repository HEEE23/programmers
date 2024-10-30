def solution(numbers):
    answer = []
    
    for n in numbers:
        bit = bin(n)[2:]
        # n이 짝수면
        if n % 2 == 0:
            bit = bit[:-1]
            bit = bit + '1'
            answer.append(int(bit,2))
        # n이 홀수면
        else:
            bit = list(bit)
            lst = list(filter(lambda x : bit[x]=='0',range(len(bit))))
            if len(lst) == 0:
                bit[0] = '0'
                bit.insert(0,'1')
            else:
                bit[lst[-1]] = '1'
                bit[lst[-1]+1] = '0'
            answer.append(int(''.join(bit),2))
        
#     방법 1. 시간초과
#     for n in numbers:
#         # 현재 수의 비트
#         bit = list(bin(n)[2:])

#         # 다른 수 
#         other_num = n
        
#        # 다른 비트의 개수
#         other_bit_cnt = 0
#         while True:
#             if other_bit_cnt > 0 and other_bit_cnt <= 2:
#                 break
#             else:
#                # 다른 비트의 개수
#                 other_bit_cnt = 0
                
#                 other_num += 1
#                 # 다른 수의 비트
#                 other_num_bit = list(bin(other_num)[2:])
#                 if len(other_num_bit) > len(bit):
#                     for i in range(len(other_num_bit)-len(bit)):
#                         bit.insert(0,'0')

#                 for i in range(len(bit)):
#                     if bit[i] != other_num_bit[i]:
#                         other_bit_cnt += 1
#                         if other_bit_cnt > 2:
#                             break

#         answer.append(other_num)
    return answer