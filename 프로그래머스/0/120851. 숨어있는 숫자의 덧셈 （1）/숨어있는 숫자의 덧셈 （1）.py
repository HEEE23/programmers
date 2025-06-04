import re
def solution(my_string):
    answer = 0
    
    my = list(map(int,''.join(re.findall('\d+', my_string))))
    answer = sum(my)
    return answer