def solution(s):
    answer = []
    
    s = list(s)
    s = s[1:-1]

    num = ''
    lst1 = [] # 리스트 내 리스트
    lst2 = [] # 리스트
    for i in s:
        if i != '}':
            if i != '{':
                if i != ',':
                    num += i
                else:
                    if len(num) != 0:
                        lst1.append(int(num))
                        num = ''
        else:
            lst1.append(int(num))
            num = ''
            lst2.append(lst1)
            lst1 = []

    # 정렬된 리스트 s
    sorted_s = sorted(lst2, key = len)
          
    for ss in sorted_s:
        for i in ss:
            if i not in answer:
                answer.append(i)
                break

    return answer