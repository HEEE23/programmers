def solution(s):
    answer = []
    
    count = 0 # 제거된 0의 개수
    translation = 0 # 이진 변환 한 수

    binary = ''
    while s != '1':
        for i in s:
            if i == '0':
                count += 1
        s = s.replace('0','')
        s = len(s)
        s = bin(s)[2:]
        translation += 1
    
    answer.extend([translation,count])
    return answer