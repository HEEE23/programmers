def solution(today, terms, privacies):
    answer = []
    today = today.replace('.','')

    terms_t = []
    terms_p = []
    for t in terms:
        lst = list(t.split(' '))
        terms_t.append(lst[0])
        terms_p.append(int(lst[1]))
    
    for i in range(len(privacies)):
        p = list(privacies[i].split(' '))
        p_date = list(map(int, p[0].split('.')))
        
        for j in range(len(terms)):
            if p[1] == terms_t[j]:
                p_date[1] += terms_p[j]
                while p_date[1] > 12:
                    p_date[0] += 1
                    p_date[1] -= 12

        p_date = list(map(str,p_date))      
        for k in (1,2):
            if len(p_date[k]) < 2:
                p_date[k] = p_date[k].zfill(2)

        privacy = ''.join(map(str,p_date))
        if privacy <= today:
            answer.append(i+1)
    
    return answer