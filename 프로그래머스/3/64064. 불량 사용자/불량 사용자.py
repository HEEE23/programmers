from itertools import permutations

def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False
    
        for j in range(len(users[i])):
            if banned_id[i][j] == '*':
                continue
            
            if banned_id[i][j] != users[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    answer = 0
    
    user_permutations = list(permutations(user_id, len(banned_id)))
    error = []
    
    for users in user_permutations:
        if not check(users, banned_id):
            continue
        else:
            users = set(users)
            if users not in error:
                error.append(users)
                
    answer = len(error)
    
#     error = []
#     for b in banned_id:
#         idx = []
#         # *이 존재하는 인덱스 위치
#         for i in range(len(b)):
#             if b[i] == '*':
#                 idx.append(i)
                
#         # user_id에 해당 인덱스 위치에 *로 문자열 교체
#         lst = []
#         for u in user_id:
#             lst.append(list(u))
            
#         for i in range(len(lst)):
#             for j in idx:
#                 if len(lst[i])-1 >= j:
#                     lst[i][j] = '*'

#         # 제재 아이디와 일치하면 리스트 추가
#         e = []
#         for i in range(len(lst)):
#             if ''.join(lst[i]) == b:
#                 e.append(user_id[i])
        
#         error.append(e)
#     print(error)

    return answer