def solution(ingredient):
    answer = 0

#     시간초과
#     ham = '1231'
#     ingredient = ''.join(map(str,ingredient))

#     while 1:
#         if ham in ingredient:
#             ingredient = ingredient.replace(ham, '',1)
#             answer += 1
#         else:
#             break

    ham = []
    for i in ingredient:
        ham.append(i)
        if ham[-4:] == [1,2,3,1]:
            answer += 1
            del ham[-4:]
    
    return answer
