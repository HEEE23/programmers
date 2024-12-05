from collections import Counter

def solution(picks, minerals):
    answer = 0
    
    if len(minerals) > 5*sum(picks):
        minerals = minerals[:5*sum(picks)]
    
    m = []
    
    for i in range(0, len(minerals), 5):
        cnt = Counter(minerals[i:i+5])
        m.append((cnt['diamond'],cnt['iron'],cnt['stone']))

    m.sort(reverse =True)

    for dia, iron, stone in m:
        if picks[0] > 0:
            answer += (dia*1 + iron*1 + stone*1)
            picks[0] -= 1
        elif picks[1] > 0:
            answer += (dia*5 + iron*1 + stone*1)
            picks[1] -= 1
        else:
            answer += (dia*25 + iron*5 + stone*1)
            picks[2] -= 1
            
    return answer