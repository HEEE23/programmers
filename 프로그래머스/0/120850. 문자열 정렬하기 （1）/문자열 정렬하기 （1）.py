import re
def solution(my_string):
    answer = []
    
    st = ''.join(re.findall('\d+',my_string))
    answer = sorted(list(map(int,st)))
    
    return answer

