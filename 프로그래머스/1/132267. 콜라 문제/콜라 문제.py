def solution(a, b, n):
    answer = 0
    coke_r = 0
    
    while n >= a:
        coke_r = int(n/a)*b
        answer += coke_r
        n = (int(n/a))*b+(n-a*(int(n/a)))
        print(n)
#     if a%2 == 0:
#         for i in range(0,n,a):
#             coke_r += b
#         coke_r += (n-int(n/a)*a)
#     else:
#         for i in range(a,n,a):
#             coke_r += b
#         coke_r += (n-int(n/a)*a)

#     while n >= a:
#         coke_r = int(n/a)
#         answer += coke_r
#         n = (n-(coke_r*a)+coke_r)
    return answer