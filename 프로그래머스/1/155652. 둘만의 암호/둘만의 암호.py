def solution(s, skip, index):
    answer = ''

#     skip = list(skip)    
#     for i in range(len(skip)):
#         skip[i] = ord(skip[i])

#     for st in s:
#         lst = []
#         for i in range(1,index+1):
#             lst.append(ord('a') + (ord(st) - ord('a') + i) % 26)
            
#         count = 0
#         for l in lst:
#             if l in skip:
#                 count += 1
#         answer += chr(ord('a') + (lst[index-1] - ord('a') + count) % 26)

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z']
    skip = list(skip)
    
    for sk in skip:
        if sk in alphabet:
            alphabet.remove(sk)

    for st in s:
        answer += alphabet[(alphabet.index(st) + index)%len(alphabet)]
    
    return answer