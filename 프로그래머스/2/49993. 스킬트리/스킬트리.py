def solution(skill, skill_trees):
    answer = 0
    
    for i in skill_trees:
        str = ''
        for j in i:
            if j in skill:
                str += j
        if skill[:len(str)] == str:
            answer += 1

    return answer