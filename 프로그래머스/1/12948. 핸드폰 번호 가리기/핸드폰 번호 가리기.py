def solution(phone_number):
    answer = ''
   
    result = phone_number[-4:]
    phone_number = list(map(int, str(phone_number)))
    
    lst = []
    for i in range(len(phone_number) - 4):
        lst.append("*")
    result = ''.join(lst)+result
    answer = result
    return answer