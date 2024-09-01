def solution(clothes):
    answer = 0
    
    clothes_dic = {} # 의상 종류 개수
    clothes_type = [] # 의상의 종류
    for i in range(len(clothes)):
        clothes_type.append(clothes[i][1])
        if clothes[i][1] in clothes_dic:
            clothes_dic[clothes[i][1]] += 1
        else:
            clothes_dic[clothes[i][1]] = 1
    
    # 중복제거
    clothes_type = list(set(clothes_type))
    
    # 하루에 최소 한 개 의상
    answer += len(clothes)
    
    # 각 종류별로 착용한 의상 조합 개수
    for i in range(len(clothes_type)-1):
        lst = clothes_type[i+1:]
        combination = 1
        for l in lst:
            combination *= (clothes_dic[l]+1)
        answer += clothes_dic[clothes_type[i]]*(combination-1)

    return answer