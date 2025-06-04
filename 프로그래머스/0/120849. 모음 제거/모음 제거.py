def solution(my_string):
    answer = ''
    
    vowels = ['a','e','i','o','u']
    for v in vowels:
        my_string = my_string.replace(v,'')
    
    answer = my_string
    return answer