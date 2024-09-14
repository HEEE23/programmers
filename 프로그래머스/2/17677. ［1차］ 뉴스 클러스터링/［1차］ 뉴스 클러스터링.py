def solution(str1, str2):
    answer = 0
    
    str1 = str1.upper()
    str2 = str2.upper()
    
    # 전체
    lst = []
    
    # str1
    lst1 = []
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            lst1.append(str1[i:i+2])
            if str1[i:i+2] not in lst:
                lst.append(str1[i:i+2])
        else:
            continue

    # str2
    lst2 = []
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            lst2.append(str2[i:i+2])
            if str2[i:i+2] not in lst:
                lst.append(str2[i:i+2])
        else:
            continue

    intersection = 0
    union = 0
    
    for l in lst:
        intersection += min(lst1.count(l), lst2.count(l))
        union += max(lst1.count(l), lst2.count(l))
    
    if intersection == 0 and union == 0:
        intersection = 1
        union = 1
        
    answer = int(intersection/union * 65536)
    return answer